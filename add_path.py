# adds to the path in /etc/environment

import sys
env = "/etc/environment"
line = open( env ).readlines()[ 0 ]
for x in sys.argv[ 1 : ]:
   if line.find( x ) < 0:
      line = line.replace( 'PATH="', 'PATH="' + x + ':' )
open( env, "w" ).write( line )
