import os
import json
from ranging import Swarmbee
from peers import Target
import utime as time


sync_word = 1
target_ = None
reset_ = False
save = False
range_amount = 1

target_list = []

# usr_args = parser.parse_args()

for filename in os.listdir():
    if filename.startswith('TARGET_CFG.txt'):
        for line in open(filename, 'r'):
            if line.startswith('Target='):
                try:
                    target_ = int(line.strip('Target='), 16)
                    target_list.append(target_)
                except AttributeError:
                    target_ = None
                print('Target:', target_)
            elif 'Range_Amount=' in line:
                range_amount = int(line.strip('Range_Amount='))
                print('Range_Amount:', range_amount)
            elif 'Sync_Word=' in line:
                sync_word = int(line.strip('Sync_Word='))
                print('Sync_Word:', sync_word)
            elif 'Reset' in line:
                reset_ = eval(line.strip('Reset='))
                print('Reset:', reset_)
            elif 'Save' in line:
                save = eval(line.strip('Save='))
                print('Save:', save)


me = Swarmbee(reset=reset_, verbose_mode=True)
# me.get_fac_settings(verbose_mode=True)
if not reset_:
    me.configure(syncword=sync_word, verbose_mode=True)
    me.get_fac_settings(reset=False, verbose_mode=True)
# if save:
#     me.save()

if target_ is not None:
       
    while(True):
        
        for target_ in target_list:
                    
            print("-" * 30)

        # for cmd_ in usr_args.cmd:
        #     me.cont_read(cmd_, verbose=True)
        
            print('ranging {} times {:012X}'.format(range_amount, target_))
            tar_get = Target(target_, 30, hint='Setup for Hackathon')
            ranges = []
            for i in range(range_amount):
                rr = me.range(tar_get)
                print("#{:>3d}:".format(i), rr)
                ranges.append(rr)
                time.sleep_ms(250)

            if range_amount > 1:
                r_res = []

                for range_ in ranges:
                    try:
                        rr_ = range_.distance
                    except AttributeError:
                        continue
                    else:
                        r_res.append(rr_)
                try:
                    print("{} ranges: {:.1f} cm [{} ... {}]".format(len(ranges), sum(r_res) / len(ranges), min(r_res), max(r_res)))
                    average_range = sum(r_res) / len(ranges)
                    output = {hex(target_): average_range}
                
                    with open('output.json', 'a') as outfile:
                        json.dump(output, outfile)
                        outfile.close()
                
                except ValueError:
                    ...
                except ZeroDivisionError:
                    print('No Ranges received!')
                    
        
        #Send json data to CPU
        #Delete json file
                    
            # me.deactivate()


def send(cmd):
    global me
    return me.cont_read(cmd)