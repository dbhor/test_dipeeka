"""Connect to the Junos OS device.
Run a show | compare CLI command.
If there is a candidate configuration, execute a rollback.
 Close the connection to the Junos OS device.
An operator has been making configuration changes without committing the configurations.
When a second operator makes a different configuration change and commits,
that second operator will be committing both configurations. Problems ensue
"""

from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from pprint import pprint
dev = Device(host="10.2.9.8", user= "", password="", gather_facts= False)
dev.open()
cu= Config(dev) ##To enter configuration mode
diff= cu.diff()  ##running show pipe compare
pprint(diff)
if diff:      ##If there is a candidate config, execute rollback
    cu.rollback()    ### perform rollback
dev.close()    ## close the connection to Junos device


