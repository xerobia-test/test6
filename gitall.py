#gitall

#commits ALL files, pushes all to cloud

#does commit -a 
#does git push
import argparse
from subprocess import *

parser = argparse.ArgumentParser()
parser.add_argument("Version_Notes", help="the message/notes for this release",
                    nargs="+", default = "Automated Message")

args = parser.parse_args()

print args.Version_Notes

try:
    check_output('git commit -a -m "{}"'.format(args.Version_Notes), shell = True, stderr=STDOUT)
    print "Local Commit Finished with message: " + args.Version_Notes
    print "Begining Push to server"
    check_output('git push', shell = True, stderr=STDOUT)
    print "Finished Push"

except CalledProcessError as error:
    print "failed"
    print "this was teh error message: "
    print error.output
    print ""
    print "please ensure that you are running this from the dir that contains the appropriate git"