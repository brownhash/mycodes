#instance families converted- c4 c5 m4 m5 m5a t2 t3 t3a r4 r5
#instance reference- https://aws.amazon.com/ec2/instance-types/

def instanceEquivalence(instances):
    keys=[]
    values=[]
    result={}
    for i in instances:
# for t2 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        if('t2' in i):
            if(i == 't2.nano'):
                if('t2.nano' in keys):
                    index=keys.index('t2.nano')
                    values[index]+=instances.get(i)
                else:
                    keys.append('t2.nano')
                    values.append(instances.get(i))
            elif(i == 't2.micro'):
                if('t2.nano' in keys):
                    index=keys.index('t2.nano')
                    values[index]+=(instances.get(i)*2)
                else:
                    keys.append('t2.micro')
                    values.append(instances.get(i)*2)
            elif (i == 't2.small'):
                if ('t2.nano' in keys):
                    index = keys.index('t2.nano')
                    values[index] += (instances.get(i)*4)
                else:
                    keys.append('t2.nano')
                    values.append(instances.get(i)*4)
            elif (i == 't2.medium'):
                if ('t2.nano' in keys):
                    index = keys.index('t2.nano')
                    values[index] += (instances.get(i)*8)
                else:
                    keys.append('t2.nano')
                    values.append(instances.get(i)*8)
            elif (i == 't2.large'):
                if ('t2.nano' in keys):
                    index = keys.index('t2.nano')
                    values[index] += (instances.get(i)*16)
                else:
                    keys.append('t2.nano')
                    values.append(instances.get(i)*16)
            elif (i == 't2.xlarge'):
                if ('t2.nano' in keys):
                    index = keys.index('t2.nano')
                    values[index] += (instances.get(i)*32)
                else:
                    keys.append('t2.nano')
                    values.append(instances.get(i)*32)
            elif (i == 't2.2xlarge'):
                if ('t2.nano' in keys):
                    index = keys.index('t2.nano')
                    values[index] += (instances.get(i)*64)
                else:
                    keys.append('t2.nano')
                    values.append(instances.get(i)*64)
# for t3 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        elif (('t3' in i) and ('t3a' not in i)):
            if (i == 't3.nano'):
                if ('t3.nano' in keys):
                    index = keys.index('t3.nano')
                    values[index] += instances.get(i)
                else:
                    keys.append('t3.nano')
                    values.append(instances.get(i))
            elif (i == 't3.micro'):
                if ('t3.nano' in keys):
                    index = keys.index('t3.nano')
                    values[index] += (instances.get(i)*2)
                else:
                    keys.append('t3.nano')
                    values.append(instances.get(i)*2)
            elif (i == 't3.small'):
                if ('t3.nano' in keys):
                    index = keys.index('t3.nano')
                    values[index] += (instances.get(i)*4)
                else:
                    keys.append('t3.nano')
                    values.append(instances.get(i)*4)
            elif (i == 't3.medium'):
                if ('t3.nano' in keys):
                    index = keys.index('t3.nano')
                    values[index] += (instances.get(i)*8)
                else:
                    keys.append('t3.nano')
                    values.append(instances.get(i)*8)
            elif (i == 't3.large'):
                if ('t3.nano' in keys):
                    index = keys.index('t3.nano')
                    values[index] += (instances.get(i)*16)
                else:
                    keys.append('t3.nano')
                    values.append(instances.get(i)*16)
            elif (i == 't3.xlarge'):
                if ('t3.nano' in keys):
                    index = keys.index('t3.nano')
                    values[index] += (instances.get(i)*32)
                else:
                    keys.append('t3.nano')
                    values.append(instances.get(i)*32)
            elif (i == 't3.2xlarge'):
                if ('t3.nano' in keys):
                    index = keys.index('t3.nano')
                    values[index] += (instances.get(i)*64)
                else:
                    keys.append('t3.nano')
                    values.append(instances.get(i)*64)
# for t3a - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        elif ('t3a' in i):
            if (i == 't3a.nano'):
                if ('t3a.nano' in keys):
                    index = keys.index('t3a.nano')
                    values[index] += instances.get(i)
                else:
                    keys.append('t3a.nano')
                    values.append(instances.get(i))
            elif (i == 't3a.micro'):
                if ('t3a.nano' in keys):
                    index = keys.index('t3a.nano')
                    values[index] += (instances.get(i)*2)
                else:
                    keys.append('t3a.nano')
                    values.append(instances.get(i)*2)
            elif (i == 't3a.small'):
                if ('t3a.nano' in keys):
                    index = keys.index('t3a.nano')
                    values[index] += (instances.get(i)*4)
                else:
                    keys.append('t3a.nano')
                    values.append(instances.get(i)*4)
            elif (i == 't3a.medium'):
                if ('t3a.nano' in keys):
                    index = keys.index('t3a.nano')
                    values[index] += (instances.get(i)*8)
                else:
                    keys.append('t3a.nano')
                    values.append(instances.get(i)*8)
            elif (i == 't3a.large'):
                if ('t3a.nano' in keys):
                    index = keys.index('t3a.nano')
                    values[index] += (instances.get(i)*16)
                else:
                    keys.append('t3a.nano')
                    values.append(instances.get(i)*16)
            elif (i == 't3a.xlarge'):
                if ('t3a.nano' in keys):
                    index = keys.index('t3a.nano')
                    values[index] += (instances.get(i)*32)
                else:
                    keys.append('t3a.nano')
                    values.append(instances.get(i)*32)
            elif (i == 't3a.2xlarge'):
                if ('t3a.nano' in keys):
                    index = keys.index('t3a.nano')
                    values[index] += (instances.get(i)*64)
                else:
                    keys.append('t3a.nano')
                    values.append(instances.get(i)*64)
# for m4 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        elif ('m4' in i):
            if (i == 'm4.large'):
                if ('m4.large' in keys):
                    index = keys.index('m4.large')
                    values[index] += instances.get(i)
                else:
                    keys.append('m4.large')
                    values.append(instances.get(i))
            elif (i == 'm4.xlarge'):
                if ('m4.large' in keys):
                    index = keys.index('m4.large')
                    values[index] += (instances.get(i)*2)
                else:
                    keys.append('m4.large')
                    values.append(instances.get(i)*2)
            elif (i == 'm4.2xlarge'):
                if ('m4.large' in keys):
                    index = keys.index('m4.large')
                    values[index] += (instances.get(i)*4)
                else:
                    keys.append('m4.large')
                    values.append(instances.get(i)*4)
            elif (i == 'm4.4xlarge'):
                if ('m4.large' in keys):
                    index = keys.index('m4.large')
                    values[index] += (instances.get(i)*8)
                else:
                    keys.append('m4.large')
                    values.append(instances.get(i)*8)
            elif (i == 'm4.10xlarge'):
                if ('m4.large' in keys):
                    index = keys.index('m4.large')
                    values[index] += (instances.get(i)*20)
                else:
                    keys.append('m4.large')
                    values.append(instances.get(i)*20)
            elif (i == 'm4.16xlarge'):
                if ('m4.large' in keys):
                    index = keys.index('m4.large')
                    values[index] += (instances.get(i)*32)
                else:
                    keys.append('m4.large')
                    values.append(instances.get(i)*32)
# for m5 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        elif (('m5' in i) and ('m5a' not in i)):
            if (i == 'm5.large'):
                if ('m5.large' in keys):
                    index = keys.index('m5.large')
                    values[index] += instances.get(i)
                else:
                    keys.append('m5.large')
                    values.append(instances.get(i))
            elif (i == 'm5.xlarge'):
                if ('m5.large' in keys):
                    index = keys.index('m5.large')
                    values[index] += (instances.get(i)*2)
                else:
                    keys.append('m5.large')
                    values.append(instances.get(i)*2)
            elif (i == 'm5.2xlarge'):
                if ('m5.large' in keys):
                    index = keys.index('m5.large')
                    values[index] += (instances.get(i)*4)
                else:
                    keys.append('m5.large')
                    values.append(instances.get(i)*4)
            elif (i == 'm5.4xlarge'):
                if ('m5.large' in keys):
                    index = keys.index('m5.large')
                    values[index] += (instances.get(i)*8)
                else:
                    keys.append('m5.large')
                    values.append(instances.get(i)*8)
            elif (i == 'm5.8xlarge'):
                if ('m5.large' in keys):
                    index = keys.index('m5.large')
                    values[index] += (instances.get(i)*16)
                else:
                    keys.append('m5.large')
                    values.append(instances.get(i)*16)
            elif (i == 'm5.12xlarge'):
                if ('m5.large' in keys):
                    index = keys.index('m5.large')
                    values[index] += (instances.get(i)*24)
                else:
                    keys.append('m5.large')
                    values.append(instances.get(i)*24)
            elif (i == 'm5.16xlarge'):
                if ('m5.large' in keys):
                    index = keys.index('m5.large')
                    values[index] += (instances.get(i)*32)
                else:
                    keys.append('m5.large')
                    values.append(instances.get(i)*32)
            elif (i == 'm5.24xlarge'):
                if ('m5.large' in keys):
                    index = keys.index('m5.large')
                    values[index] += (instances.get(i)*48)
                else:
                    keys.append('m5.large')
                    values.append(instances.get(i)*48)
            elif (i == 'm5.metal'):
                if ('m5.large' in keys):
                    index = keys.index('m5.large')
                    values[index] += (instances.get(i)*48)
                else:
                    keys.append('m5.large')
                    values.append(instances.get(i)*48)
# for m5a - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        elif ('m5a' in i):
            if (i == 'm5a.large'):
                if ('m5a.large' in keys):
                    index = keys.index('m5a.large')
                    values[index] += instances.get(i)
                else:
                    keys.append('m5a.large')
                    values.append(instances.get(i))
            elif (i == 'm5a.xlarge'):
                if ('m5a.large' in keys):
                    index = keys.index('m5a.large')
                    values[index] += (instances.get(i)*2)
                else:
                    keys.append('m5a.large')
                    values.append(instances.get(i)*2)
            elif (i == 'm5a.2xlarge'):
                if ('m5a.large' in keys):
                    index = keys.index('m5a.large')
                    values[index] += (instances.get(i)*4)
                else:
                    keys.append('m5a.large')
                    values.append(instances.get(i)*4)
            elif (i == 'm5a.4xlarge'):
                if ('m5a.large' in keys):
                    index = keys.index('m5a.large')
                    values[index] += (instances.get(i)*8)
                else:
                    keys.append('m5a.large')
                    values.append(instances.get(i)*8)
            elif (i == 'm5a.8xlarge'):
                if ('m5a.large' in keys):
                    index = keys.index('m5a.large')
                    values[index] += (instances.get(i)*16)
                else:
                    keys.append('m5a.large')
                    values.append(instances.get(i)*16)
            elif (i == 'm5a.12xlarge'):
                if ('m5a.large' in keys):
                    index = keys.index('m5a.large')
                    values[index] += (instances.get(i)*24)
                else:
                    keys.append('m5a.large')
                    values.append(instances.get(i)*24)
            elif (i == 'm5a.16xlarge'):
                if ('m5a.large' in keys):
                    index = keys.index('m5a.large')
                    values[index] += (instances.get(i)*32)
                else:
                    keys.append('m5a.large')
                    values.append(instances.get(i)*32)
            elif (i == 'm5a.24xlarge'):
                if ('m5a.large' in keys):
                    index = keys.index('m5a.large')
                    values[index] += (instances.get(i)*48)
                else:
                    keys.append('m5a.large')
                    values.append(instances.get(i)*48)
# for c5 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        elif ('c5' in i):
            if (i == 'c5.large'):
                if ('c5.large' in keys):
                    index = keys.index('c5.large')
                    values[index] += instances.get(i)
                else:
                    keys.append('c5.large')
                    values.append(instances.get(i))
            elif (i == 'c5.xlarge'):
                if ('c5.large' in keys):
                    index = keys.index('c5.large')
                    values[index] += (instances.get(i)*2)
                else:
                    keys.append('c5.large')
                    values.append(instances.get(i)*2)
            elif (i == 'c5.2xlarge'):
                if ('c5.large' in keys):
                    index = keys.index('c5.large')
                    values[index] += (instances.get(i)*4)
                else:
                    keys.append('c5.large')
                    values.append(instances.get(i)*4)
            elif (i == 'c5.4xlarge'):
                if ('c5.large' in keys):
                    index = keys.index('c5.large')
                    values[index] += (instances.get(i)*8)
                else:
                    keys.append('c5.large')
                    values.append(instances.get(i)*8)
            elif (i == 'c5.9xlarge'):
                if ('c5.large' in keys):
                    index = keys.index('c5.large')
                    values[index] += (instances.get(i)*18)
                else:
                    keys.append('c5.large')
                    values.append(instances.get(i)*18)
            elif (i == 'c5.12xlarge'):
                if ('c5.large' in keys):
                    index = keys.index('c5.large')
                    values[index] += (instances.get(i)*24)
                else:
                    keys.append('c5.large')
                    values.append(instances.get(i)*24)
            elif (i == 'c5.18xlarge'):
                if ('c5.large' in keys):
                    index = keys.index('c5.large')
                    values[index] += (instances.get(i)*36)
                else:
                    keys.append('c5.large')
                    values.append(instances.get(i)*36)
            elif (i == 'c5.24xlarge'):
                if ('c5.large' in keys):
                    index = keys.index('c5.large')
                    values[index] += (instances.get(i)*48)
                else:
                    keys.append('c5.large')
                    values.append(instances.get(i)*48)
# for c4 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        elif ('c4' in i):
            if (i == 'c4.large'):
                if ('c4.large' in keys):
                    index = keys.index('c4.large')
                    values[index] += instances.get(i)
                else:
                    keys.append('c4.large')
                    values.append(instances.get(i))
            elif (i == 'c4.xlarge'):
                if ('c4.large' in keys):
                    index = keys.index('c4.large')
                    values[index] += (instances.get(i)*2)
                else:
                    keys.append('c4.large')
                    values.append(instances.get(i)*2)
            elif (i == 'c4.2xlarge'):
                if ('c4.large' in keys):
                    index = keys.index('c4.large')
                    values[index] += (instances.get(i)*4)
                else:
                    keys.append('c4.large')
                    values.append(instances.get(i)*4)
            elif (i == 'c4.4xlarge'):
                if ('c4.large' in keys):
                    index = keys.index('c4.large')
                    values[index] += (instances.get(i)*8)
                else:
                    keys.append('c4.large')
                    values.append(instances.get(i)*8)
            elif (i == 'c4.8xlarge'):
                if ('c4.large' in keys):
                    index = keys.index('c4.large')
                    values[index] += (instances.get(i)*16)
                else:
                    keys.append('c4.large')
                    values.append(instances.get(i)*16)
# for r4 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        elif ('r4' in i):
            if (i == 'r4.large'):
                if ('r4.large' in keys):
                    index = keys.index('r4.large')
                    values[index] += instances.get(i)
                else:
                    keys.append('r4.large')
                    values.append(instances.get(i))
            elif (i == 'r4.xlarge'):
                if ('r4.large' in keys):
                    index = keys.index('r4.large')
                    values[index] += (instances.get(i)*2)
                else:
                    keys.append('r4.large')
                    values.append(instances.get(i)*2)
            elif (i == 'r4.2xlarge'):
                if ('r4.large' in keys):
                    index = keys.index('r4.large')
                    values[index] += (instances.get(i)*4)
                else:
                    keys.append('r4.large')
                    values.append(instances.get(i)*4)
            elif (i == 'r4.4xlarge'):
                if ('r4.large' in keys):
                    index = keys.index('r4.large')
                    values[index] += (instances.get(i)*8)
                else:
                    keys.append('r4.large')
                    values.append(instances.get(i)*8)
            elif (i == 'r4.8xlarge'):
                if ('r4.large' in keys):
                    index = keys.index('r4.large')
                    values[index] += (instances.get(i)*16)
                else:
                    keys.append('r4.large')
                    values.append(instances.get(i)*16)
            elif (i == 'r4.16xlarge'):
                if ('r4.large' in keys):
                    index = keys.index('r4.large')
                    values[index] += (instances.get(i)*32)
                else:
                    keys.append('r4.large')
                    values.append(instances.get(i)*32)
# for r5 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        elif (('r5' in i) and ('r5a' not in i)):
            if (i == 'r5.large'):
                if ('r5.large' in keys):
                    index = keys.index('r5.large')
                    values[index] += instances.get(i)
                else:
                    keys.append('r5.large')
                    values.append(instances.get(i))
            elif (i == 'r5.xlarge'):
                if ('r5.large' in keys):
                    index = keys.index('r5.large')
                    values[index] += (instances.get(i)*2)
                else:
                    keys.append('r5.large')
                    values.append(instances.get(i)*2)
            elif (i == 'r5.2xlarge'):
                if ('r5.large' in keys):
                    index = keys.index('r5.large')
                    values[index] += (instances.get(i)*4)
                else:
                    keys.append('r5.large')
                    values.append(instances.get(i)*4)
            elif (i == 'r5.4xlarge'):
                if ('r5.large' in keys):
                    index = keys.index('r5.large')
                    values[index] += (instances.get(i)*8)
                else:
                    keys.append('r5.large')
                    values.append(instances.get(i)*8)
            elif (i == 'r5.8xlarge'):
                if ('r5.large' in keys):
                    index = keys.index('r5.large')
                    values[index] += (instances.get(i)*16)
                else:
                    keys.append('r5.large')
                    values.append(instances.get(i)*16)
            elif (i == 'r5.12xlarge'):
                if ('r5.large' in keys):
                    index = keys.index('r5.large')
                    values[index] += (instances.get(i)*24)
                else:
                    keys.append('r5.large')
                    values.append(instances.get(i)*24)
            elif (i == 'r5.16xlarge'):
                if ('r5.large' in keys):
                    index = keys.index('r5.large')
                    values[index] += (instances.get(i)*32)
                else:
                    keys.append('r5.large')
                    values.append(instances.get(i)*32)
            elif (i == 'r5.24xlarge'):
                if ('r5.large' in keys):
                    index = keys.index('r5.large')
                    values[index] += (instances.get(i)*48)
                else:
                    keys.append('r5.large')
                    values.append(instances.get(i)*48)
# for r5a - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        elif ('r5a' in i):
            if (i == 'r5a.large'):
                if ('r5a.large' in keys):
                    index = keys.index('r5a.large')
                    values[index] += instances.get(i)
                else:
                    keys.append('r5a.large')
                    values.append(instances.get(i))
            elif (i == 'r5a.xlarge'):
                if ('r5a.large' in keys):
                    index = keys.index('r5a.large')
                    values[index] += (instances.get(i)*2)
                else:
                    keys.append('r5a.large')
                    values.append(instances.get(i)*2)
            elif (i == 'r5a.2xlarge'):
                if ('r5a.large' in keys):
                    index = keys.index('r5a.large')
                    values[index] += (instances.get(i)*4)
                else:
                    keys.append('r5a.large')
                    values.append(instances.get(i)*4)
            elif (i == 'r5a.4xlarge'):
                if ('r5a.large' in keys):
                    index = keys.index('r5a.large')
                    values[index] += (instances.get(i)*8)
                else:
                    keys.append('r5a.large')
                    values.append(instances.get(i)*8)
            elif (i == 'r5a.8xlarge'):
                if ('r5a.large' in keys):
                    index = keys.index('r5a.large')
                    values[index] += (instances.get(i)*16)
                else:
                    keys.append('r5a.large')
                    values.append(instances.get(i)*16)
            elif (i == 'r5a.12xlarge'):
                if ('r5a.large' in keys):
                    index = keys.index('r5a.large')
                    values[index] += (instances.get(i)*24)
                else:
                    keys.append('r5a.large')
                    values.append(instances.get(i)*24)
            elif (i == 'r5a.16xlarge'):
                if ('r5a.large' in keys):
                    index = keys.index('r5a.large')
                    values[index] += (instances.get(i)*32)
                else:
                    keys.append('r5a.large')
                    values.append(instances.get(i)*32)
            elif (i == 'r5a.24xlarge'):
                if ('r5a.large' in keys):
                    index = keys.index('r5a.large')
                    values[index] += (instances.get(i)*48)
                else:
                    keys.append('r5a.large')
                    values.append(instances.get(i)*48)
# for every other instance - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        else:
            if (i in keys):
                index = keys.index(i)
                values[index] += instances.get(i)
            else:
                keys.append(i)
                values.append(instances.get(i))

    for i in range(0,len(keys)):
        key=keys[i]
        val=values[i]
        result[key]=val

    return (result)
