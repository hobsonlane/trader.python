import sys
import os
import json
import json_ascii
from bitfloor import RAPI

def get_rapi():
    if len(sys.argv) < 3: 
        print "Usage: {0} product_id keyfile".format(sys.argv[0])
        #sys.exit(1)
    if len(sys.argv) > 2:
        path = sys.argv[2]
    else:
        path = os.path.join(os.path.join('/etc','security','bfl.json'))
    if len(sys.argv) > 1:
        product_id = sys.argv[1]
    else:
        product_id = 1  # BTCUSD

    with open(path) as f:
        config = json.load(f, object_hook=json_ascii.decode_dict)

    return RAPI(product_id=product_id, key=config['key'], secret=config['secret'])
