#instance families converted- c4 c5 m4 m5 m5a t2 t3 t3a r4 r5
#instance reference- https://aws.amazon.com/ec2/instance-types/

def instanceEquivalence(instances):
    result={}
    ri_instance_types ={
                    't2': {
                        'unit':'t2.nano', # Base unit type - to be used in message
                        'instance_types':{
                                    't2.nano': 1,
                                    't2.micro': 2,
                                    't2.small': 4,
                                    't2.medium': 8,
                                    't2.large': 16,
                                    't2.xlarge': 32,
                                    't2.2xlarge': 64
                        }
                    },
                    't3': {
                        'unit': 't3.nano', # Base unit type - to be used in message
                        'instance_types': {
                                    't3.nano': 1,
                                    't3.micro': 2,
                                    't3.small': 4,
                                    't3.medium': 8,
                                    't3.large': 16,
                                    't3.xlarge': 32,
                                    't3.2xlarge': 64
                        }
                    },
                    't3a': {
                        'unit': 't3a.nano', # Base unit type - to be used in message
                        'instance_types': {
                                    't3a.nano': 1,
                                    't3a.micro': 2,
                                    't3a.small': 4,
                                    't3a.medium': 8,
                                    't3a.large': 16,
                                    't3a.xlarge': 32,
                                    't3a.2xlarge': 64
                        }
                    },
                    'm4': {
                        'unit': 'm4.large', # Base unit type - to be used in message
                        'instance_types': {
                                    'm4.large': 1,
                                    'm4.xlarge': 2,
                                    'm4.2xlarge': 4,
                                    'm4.4xlarge': 8,
                                    'm4.10xlarge': 20,
                                    'm4.16xlarge': 32
                        }
                    },
                    'm5': {
                        'unit': 'm5.large', # Base unit type - to be used in message
                        'instance_types': {
                                    'm5.large': 1,
                                    'm5.xlarge': 2,
                                    'm5.2xlarge': 4,
                                    'm5.4xlarge': 8,
                                    'm5.8xlarge': 16,
                                    'm5.12xlarge': 24,
                                    'm5.16xlarge': 32,
                                    'm5.24xlarge': 48
                        }
                    },
                    'm5a': {
                        'unit': 'm5a.large', # Base unit type - to be used in message
                        'instance_types': {
                                    'm5a.large': 1,
                                    'm5a.xlarge': 2,
                                    'm5a.2xlarge': 4,
                                    'm5a.4xlarge': 8,
                                    'm5a.8xlarge': 16,
                                    'm5a.12xlarge': 24,
                                    'm5a.16xlarge': 32,
                                    'm5a.24xlarge': 48
                        }
                    },
                    'c5': {
                        'unit': 'c5.large', # Base unit type - to be used in message
                        'instance_types': {
                                    'c5.large': 1,
                                    'c5.xlarge': 2,
                                    'c5.2xlarge': 4,
                                    'c5.4xlarge': 8,
                                    'c5.9xlarge': 18,
                                    'c5.12xlarge': 24,
                                    'c5.18xlarge': 36,
                                    'c5.24xlarge': 48
                        }
                    },
                    'c4': {
                        'unit': 'c4.large', # Base unit type - to be used in message
                        'instance_types': {
                                    'c4.large': 1,
                                    'c4.xlarge': 2,
                                    'c4.2xlarge': 4,
                                    'c4.4xlarge': 8,
                                    'c4.8xlarge': 16
                        }
                    },
                    'r4': {
                        'unit': 'r4.large', # Base unit type - to be used in message
                        'instance_types': {
                                    'r4.large': 1,
                                    'r4.xlarge': 2,
                                    'r4.2xlarge': 4,
                                    'r4.4xlarge': 8,
                                    'r4.8xlarge': 16,
                                    'r4.16xlarge': 32
                        }
                    },
                    'r5': {
                        'unit': 'r5.large', # Base unit type - to be used in message
                        'instance_types': {
                                    'r5.large': 1,
                                    'r5.xlarge': 2,
                                    'r5.2xlarge': 4,
                                    'r5.4xlarge': 8,
                                    'r5.8xlarge': 16,
                                    'r5.12xlarge': 24,
                                    'r5.16xlarge': 32,
                                    'r5.24xlarge': 48
                        }
                    },
                    'r5a': {
                        'unit': 'r5a.large', # Base unit type - to be used in message
                        'instance_types': {
                                    'r5a.large': 1,
                                    'r5a.xlarge': 2,
                                    'r5a.2xlarge': 4,
                                    'r5a.4xlarge': 8,
                                    'r5a.8xlarge': 16,
                                    'r5a.12xlarge': 24,
                                    'r5a.16xlarge': 32,
                                    'r5a.24xlarge': 48
                        }
                    }
                }
    for i in ri_instance_types:
        instance_type=ri_instance_types.get(i).get('unit')
        result[instance_type]=0

    for i in instances:
        check_i=str(i).split(".")
        instance_family=check_i[0]
        if(ri_instance_types.get(instance_family)):
            multiplier=ri_instance_types.get(instance_family).get('instance_types').get(i)
            unit=ri_instance_types.get(instance_family).get('unit')
            value=instances.get(i)*multiplier
            result[unit]=result.get(unit)+value
        else:
            result[i]=instances.get(i)

    return (result)
