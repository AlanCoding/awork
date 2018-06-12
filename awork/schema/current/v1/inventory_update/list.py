endpoint = u'inventory_updates'
name = u'Inventory Update List'
related_search_fields = [u'schedule__search',
                         u'modified_by__search',
                         u'notifications__search',
                         u'inventory_source__search',
                         u'inventory_update_events__search',
                         u'source_project_update__search',
                         u'unified_job_template__search',
                         u'unifiedjob_ptr__search',
                         u'instance_group__search',
                         u'credentials__search',
                         u'source_script__search',
                         u'unified_job_node__search',
                         u'dependent_jobs__search',
                         u'launch_config__search',
                         u'job_origin__search',
                         u'created_by__search',
                         u'labels__search']
parses = [u'application/json']
search_fields = [u'description', u'name']
actions = {u'GET': {u'controller_node': {u'filterable': True,
                                         u'help_text': u'The instance that managed the isolated execution environment.',
                                         u'label': u'Controller node',
                                         u'type': u'string'},
                    u'created': {u'filterable': True,
                                 u'help_text': u'Timestamp when this inventory update was created.',
                                 u'label': u'Created',
                                 u'type': u'datetime'},
                    u'credential': {u'help_text': u'This resource has been deprecated and will be removed in a future release',
                                    u'label': u'Credential',
                                    u'min_value': 1,
                                    u'type': u'integer'},
                    u'description': {u'filterable': True,
                                     u'help_text': u'Optional description of this inventory update.',
                                     u'label': u'Description',
                                     u'type': u'string'},
                    u'elapsed': {u'filterable': True,
                                 u'help_text': u'Elapsed time in seconds that the job ran.',
                                 u'label': u'Elapsed',
                                 u'type': u'decimal'},
                    u'execution_node': {u'filterable': True,
                                        u'help_text': u'The node the job executed on.',
                                        u'label': u'Execution node',
                                        u'type': u'string'},
                    u'failed': {u'filterable': True,
                                u'label': u'Failed',
                                u'type': u'boolean'},
                    u'finished': {u'filterable': True,
                                  u'help_text': u'The date and time the job finished execution.',
                                  u'label': u'Finished',
                                  u'type': u'datetime'},
                    u'group_by': {u'ec2_group_by_choices': [[u'ami_id', u'Image ID'],
                                                            [u'availability_zone',
                                                             u'Availability Zone'],
                                                            [u'aws_account',
                                                                u'Account'],
                                                            [u'instance_id',
                                                             u'Instance ID'],
                                                            [u'instance_state',
                                                             u'Instance State'],
                                                            [u'platform',
                                                                u'Platform'],
                                                            [u'instance_type',
                                                             u'Instance Type'],
                                                            [u'key_pair',
                                                                u'Key Name'],
                                                            [u'region', u'Region'],
                                                            [u'security_group',
                                                             u'Security Group'],
                                                            [u'tag_keys', u'Tags'],
                                                            [u'tag_none',
                                                                u'Tag None'],
                                                            [u'vpc_id', u'VPC ID']],
                                  u'filterable': True,
                                  u'help_text': u'Limit groups automatically created from inventory source (EC2 only).',
                                  u'label': u'Group by',
                                  u'type': u'string'},
                    u'id': {u'filterable': True,
                            u'help_text': u'Database ID for this inventory update.',
                            u'label': u'ID',
                            u'type': u'integer'},
                    u'instance_filters': {u'filterable': True,
                                          u'help_text': u'Comma-separated list of filter expressions (EC2 only). Hosts are imported when ANY of the filters match.',
                                          u'label': u'Instance filters',
                                          u'type': u'string'},
                    u'inventory_source': {u'filterable': True,
                                          u'label': u'Inventory source',
                                          u'type': u'field'},
                    u'job_explanation': {u'filterable': True,
                                         u'help_text': u"A status field to indicate the state of the job if it wasn't able to run and capture stdout",
                                         u'label': u'Job explanation',
                                         u'type': u'string'},
                    u'launch_type': {u'choices': [[u'manual', u'Manual'],
                                                  [u'relaunch', u'Relaunch'],
                                                  [u'callback', u'Callback'],
                                                  [u'scheduled', u'Scheduled'],
                                                  [u'dependency', u'Dependency'],
                                                  [u'workflow', u'Workflow'],
                                                  [u'sync', u'Sync'],
                                                  [u'scm', u'SCM Update']],
                                     u'filterable': True,
                                     u'label': u'Launch type',
                                     u'type': u'choice'},
                    u'license_error': {u'filterable': True,
                                       u'label': u'License error',
                                       u'type': u'boolean'},
                    u'modified': {u'filterable': True,
                                  u'help_text': u'Timestamp when this inventory update was last modified.',
                                  u'label': u'Modified',
                                  u'type': u'datetime'},
                    u'name': {u'filterable': True,
                              u'help_text': u'Name of this inventory update.',
                              u'label': u'Name',
                              u'type': u'string'},
                    u'overwrite': {u'filterable': True,
                                   u'help_text': u'Overwrite local groups and hosts from remote inventory source.',
                                   u'label': u'Overwrite',
                                   u'type': u'boolean'},
                    u'overwrite_vars': {u'filterable': True,
                                        u'help_text': u'Overwrite local variables from remote inventory source.',
                                        u'label': u'Overwrite vars',
                                        u'type': u'boolean'},
                    u'related': {u'help_text': u'Data structure with URLs of related resources.',
                                 u'label': u'Related',
                                 u'type': u'object'},
                    u'source': {u'choices': [[u'', u'Manual'],
                                             [u'file', u'File, Directory or Script'],
                                             [u'scm', u'Sourced from a Project'],
                                             [u'ec2', u'Amazon EC2'],
                                             [u'gce', u'Google Compute Engine'],
                                             [u'azure_rm',
                                              u'Microsoft Azure Resource Manager'],
                                             [u'vmware', u'VMware vCenter'],
                                             [u'satellite6', u'Red Hat Satellite 6'],
                                             [u'cloudforms', u'Red Hat CloudForms'],
                                             [u'openstack', u'OpenStack'],
                                             [u'rhv', u'Red Hat Virtualization'],
                                             [u'tower', u'Ansible Tower'],
                                             [u'custom', u'Custom Script']],
                                u'filterable': True,
                                u'label': u'Source',
                                u'type': u'choice'},
                    u'source_path': {u'filterable': True,
                                     u'label': u'Source path',
                                     u'type': u'string'},
                    u'source_project_update': {u'filterable': True,
                                               u'help_text': u'Inventory files from this Project Update were used for the inventory update.',
                                               u'label': u'Source project update',
                                               u'type': u'field'},
                    u'source_regions': {u'azure_rm_region_choices': [[u'all', u'All'],
                                                                     [u'eastus',
                                                                      u'US East'],
                                                                     [u'eastus2',
                                                                      u'US East 2'],
                                                                     [u'centralus',
                                                                      u'US Central'],
                                                                     [u'northcentralus',
                                                                      u'US North Central'],
                                                                     [u'southcentralus',
                                                                      u'US South Central'],
                                                                     [u'westcentralus',
                                                                      u'US West Central'],
                                                                     [u'westus',
                                                                      u'US West'],
                                                                     [u'westus2',
                                                                      u'US West 2'],
                                                                     [u'eastasia',
                                                                      u'Asia East'],
                                                                     [u'southestasia',
                                                                      u'Asia Southeast'],
                                                                     [u'australiaeast',
                                                                      u'Australia East'],
                                                                     [u'australiasoutheast',
                                                                      u'Australia Southeast'],
                                                                     [u'brazilsouth',
                                                                      u'Brazil South'],
                                                                     [u'canadacentral',
                                                                      u'Canada Central'],
                                                                     [u'canadaeast',
                                                                      u'Canada East'],
                                                                     [u'northeurope',
                                                                      u'Europe North'],
                                                                     [u'westeurope',
                                                                      u'Europe West'],
                                                                     [u'southindia',
                                                                      u'India South'],
                                                                     [u'westindia',
                                                                      u'India West'],
                                                                     [u'japaneast',
                                                                      u'Japan East'],
                                                                     [u'japanwest',
                                                                      u'Japan West'],
                                                                     [u'koreacentral',
                                                                      u'Korea Central'],
                                                                     [u'koreasouth',
                                                                      u'Korea South'],
                                                                     [u'uksouth',
                                                                      u'UK South'],
                                                                     [u'ukwest',
                                                                      u'UK West']],
                                        u'ec2_region_choices': [[u'all', u'All'],
                                                                [u'us-west-1',
                                                                 u'US West (Northern California)'],
                                                                [u'us-east-1',
                                                                 u'US East (Northern Virginia)'],
                                                                [u'us-east-2',
                                                                 u'US East (Ohio)'],
                                                                [u'us-west-2',
                                                                 u'US West (Oregon)'],
                                                                [u'us-gov-west-1',
                                                                 u'US West (GovCloud)'],
                                                                [u'ap-south-1',
                                                                 u'Asia Pacific (Mumbai)'],
                                                                [u'ap-northeast-2',
                                                                 u'Asia Pacific (Seoul)'],
                                                                [u'ap-southeast-1',
                                                                 u'Asia Pacific (Singapore)'],
                                                                [u'ap-southeast-2',
                                                                 u'Asia Pacific (Sydney)'],
                                                                [u'ap-northeast-1',
                                                                 u'Asia Pacific (Tokyo)'],
                                                                [u'ca-central-1',
                                                                 u'Canada (Central)'],
                                                                [u'cn-north-1',
                                                                 u'China (Beijing)'],
                                                                [u'eu-central-1',
                                                                 u'EU (Frankfurt)'],
                                                                [u'eu-west-1',
                                                                 u'EU (Ireland)'],
                                                                [u'eu-west-2',
                                                                 u'EU (London)'],
                                                                [u'sa-east-1',
                                                                 u'South America (Sao Paulo)']],
                                        u'filterable': True,
                                        u'gce_region_choices': [[u'all', u'All'],
                                                                [u'us-east1-b',
                                                                 u'US East 1 (B)'],
                                                                [u'us-east1-c',
                                                                 u'US East 1 (C)'],
                                                                [u'us-east1-d',
                                                                 u'US East 1 (D)'],
                                                                [u'us-east4-a',
                                                                 u'US East 4 (A)'],
                                                                [u'us-east4-b',
                                                                 u'US East 4 (B)'],
                                                                [u'us-east4-c',
                                                                 u'US East 4 (C)'],
                                                                [u'us-central1-a',
                                                                 u'US Central (A)'],
                                                                [u'us-central1-b',
                                                                 u'US Central (B)'],
                                                                [u'us-central1-c',
                                                                 u'US Central (C)'],
                                                                [u'us-central1-f',
                                                                 u'US Central (F)'],
                                                                [u'us-west1-a',
                                                                 u'US West (A)'],
                                                                [u'us-west1-b',
                                                                 u'US West (B)'],
                                                                [u'us-west1-c',
                                                                 u'US West (C)'],
                                                                [u'asia-east1-a',
                                                                 u'Asia East (A)'],
                                                                [u'asia-east1-b',
                                                                 u'Asia East (B)'],
                                                                [u'asia-east1-c',
                                                                 u'Asia East (C)'],
                                                                [u'asia-northeast1-a',
                                                                 u'Asia Northeast (A)'],
                                                                [u'asia-northeast1-b',
                                                                 u'Asia Northeast (B)'],
                                                                [u'asia-northeast1-c',
                                                                 u'Asia Northeast (C)'],
                                                                [u'asia-southeast1-a',
                                                                 u'Asia Southeast (A)'],
                                                                [u'asia-southeast1-b',
                                                                 u'Asia Southeast (B)'],
                                                                [u'australia-southeast1-a',
                                                                 u'Australia Southeast (A)'],
                                                                [u'australia-southeast1-b',
                                                                 u'Australia Southeast (B)'],
                                                                [u'australia-southeast1-c',
                                                                 u'Australia Southeast (C)'],
                                                                [u'europe-west1-b',
                                                                 u'Europe West 1 (B)'],
                                                                [u'europe-west1-c',
                                                                 u'Europe West 1 (C)'],
                                                                [u'europe-west1-d',
                                                                 u'Europe West 1 (D)'],
                                                                [u'europe-west2-a',
                                                                 u'Europe West 2 (A)'],
                                                                [u'europe-west2-b',
                                                                 u'Europe West 2 (B)'],
                                                                [u'europe-west2-c',
                                                                 u'Europe West 2 (C)']],
                                        u'label': u'Source regions',
                                        u'type': u'string'},
                    u'source_script': {u'filterable': True,
                                       u'label': u'Source script',
                                       u'type': u'field'},
                    u'source_vars': {u'filterable': True,
                                     u'help_text': u'Inventory source variables in YAML or JSON format.',
                                     u'label': u'Source vars',
                                     u'type': u'string'},
                    u'started': {u'filterable': True,
                                 u'help_text': u'The date and time the job was queued for starting.',
                                 u'label': u'Started',
                                 u'type': u'datetime'},
                    u'status': {u'choices': [[u'new', u'New'],
                                             [u'pending', u'Pending'],
                                             [u'waiting', u'Waiting'],
                                             [u'running', u'Running'],
                                             [u'successful', u'Successful'],
                                             [u'failed', u'Failed'],
                                             [u'error', u'Error'],
                                             [u'canceled', u'Canceled']],
                                u'filterable': True,
                                u'label': u'Status',
                                u'type': u'choice'},
                    u'summary_fields': {u'help_text': u'Data structure with name/description for related resources.',
                                        u'label': u'Summary fields',
                                        u'type': u'object'},
                    u'timeout': {u'filterable': True,
                                 u'help_text': u'The amount of time (in seconds) to run before the task is canceled.',
                                 u'label': u'Timeout',
                                 u'max_value': 2147483647,
                                 u'min_value': -2147483648,
                                 u'type': u'integer'},
                    u'type': {u'choices': [[u'inventory_update', u'Inventory Sync']],
                              u'help_text': u'Data type for this inventory update.',
                              u'label': u'Type',
                              u'type': u'choice'},
                    u'unified_job_template': {u'filterable': True,
                                              u'label': u'unified job template',
                                              u'type': u'field'},
                    u'url': {u'help_text': u'URL for this inventory update.',
                             u'label': u'Url',
                             u'type': u'string'},
                    u'verbosity': {u'choices': [[0, u'0 (WARNING)'],
                                                [1, u'1 (INFO)'],
                                                [2, u'2 (DEBUG)']],
                                   u'filterable': True,
                                   u'label': u'Verbosity',
                                   u'type': u'choice'}}}
renders = [u'application/json', u'text/html']
max_page_size = 200
types = [u'inventory_update']