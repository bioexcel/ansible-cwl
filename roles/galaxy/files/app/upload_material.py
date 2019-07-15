from bioblend.galaxy import GalaxyInstance
import json
import sys, glob

BASE_URL='http://localhost:8080'
KEY='111111111111111111111'
gi = GalaxyInstance(url=BASE_URL, key=KEY)
for filename in glob.glob('/app/workflow-is-cwl/workflows/*.cwl.packed'):
    try:
        cwl_wf = json.load(open(filename,'r'))
        gi.workflows.import_workflow_dict(cwl_wf)
    except:
        print "failed uploading %s" % filename
