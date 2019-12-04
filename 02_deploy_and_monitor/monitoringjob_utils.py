from sagemaker.processing import Processor, ProcessingInput, ProcessingOutput

def get_model_monitor_container_uri(region):
    container_uri_format = '{0}.dkr.ecr.{1}.amazonaws.com/sagemaker-model-monitor-analyzer'
    
    regions_to_accounts = {
        'eu-north-1': '895015795356',
        'me-south-1': '607024016150',
        'ap-south-1': '126357580389',
        'us-east-2': '680080141114',
        'us-east-2': '777275614652',
        'eu-west-1': '468650794304',
        'eu-central-1': '048819808253',
        'sa-east-1': '539772159869',
        'ap-east-1': '001633400207',
        'us-east-1': '156813124566',
        'ap-northeast-2': '709848358524',
        'eu-west-2': '749857270468',
        'ap-northeast-1': '574779866223',
        'us-west-2': '159807026194',
        'us-west-1': '890145073186',
        'ap-southeast-1': '245545462676',
        'ap-southeast-2': '563025443158',
        'ca-central-1': '536280801234'
    }
    
    container_uri = container_uri_format.format(regions_to_accounts[region], region)
    return container_uri

def run_model_monitor_job_processor(region, instance_type, role, data_capture_path, preprocessor_path, postprocessor_path,
                                   statistics_path, constraints_path, reports_path):
    
    data_capture_sub_path = data_capture_path[data_capture_path.rfind('datacapture/') :]
    data_capture_sub_path = data_capture_sub_path[data_capture_sub_path.find('/') + 1 :]
    processing_output_paths = reports_path + '/' + data_capture_sub_path
    
    input_1 = ProcessingInput(input_name='input_1',
                          source=data_capture_path,
                          destination='/opt/ml/processing/input/endpoint/' + data_capture_sub_path,
                          s3_data_type='S3Prefix',
                          s3_input_mode='File')

    baseline = ProcessingInput(input_name='baseline',
                               source=statistics_path,
                               destination='/opt/ml/processing/baseline/stats',
                               s3_data_type='S3Prefix',
                               s3_input_mode='File')

    constraints = ProcessingInput(input_name='constraints',
                                  source=constraints_path,
                                  destination='/opt/ml/processing/baseline/constraints',
                                  s3_data_type='S3Prefix',
                                  s3_input_mode='File')

    post_processor_script = ProcessingInput(input_name='post_processor_script',
                                            source=postprocessor_path,
                                            destination='/opt/ml/processing/code/postprocessing',
                                            s3_data_type='S3Prefix',
                                            s3_input_mode='File')

    pre_processor_script = ProcessingInput(input_name='pre_processor_script',
                                           source=preprocessor_path,
                                           destination='/opt/ml/processing/code/preprocessing',
                                           s3_data_type='S3Prefix',
                                           s3_input_mode='File')

    outputs = ProcessingOutput(output_name='result',
                               source='/opt/ml/processing/output',
                               destination=processing_output_paths,
                               s3_upload_mode='Continuous')

    processor = Processor(image_uri = get_model_monitor_container_uri(region),
                          instance_count = 1,
                          instance_type = instance_type,
                          role=role,
                          env = {
                              'baseline_constraints': '/opt/ml/processing/baseline/constraints/constraints.json',
                              'baseline_statistics': '/opt/ml/processing/baseline/stats/statistics.json',
                              'dataset_format': '{"sagemakerCaptureJson":{"captureIndexNames":["endpointInput","endpointOutput"]}}',
                              'dataset_source': '/opt/ml/processing/input/endpoint',
                              'output_path': '/opt/ml/processing/output',
                              'post_analytics_processor_script': '/opt/ml/processing/code/postprocessing/postprocessor.py',
                              'publish_cloudwatch_metrics': 'Disabled',
                              'record_preprocessor_script': '/opt/ml/processing/code/preprocessing/preprocessor.py'
                          })
    
    return processor.run(inputs=[input_1, baseline, constraints, post_processor_script, pre_processor_script],
             outputs=[outputs])