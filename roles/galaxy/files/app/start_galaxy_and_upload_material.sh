set -m
. /app/galaxy/.venv/bin/activate
for filename in /app/workflow-is-cwl/workflows/*.cwl; do
    cwltool --pack $filename > "$filename.packed"
    done
sh /app/start.sh &
GALAXY_PID=$! 
echo "Galaxy PID is $GALAXY_PID"
wait-for-it/wait-for-it.sh -t 240 localhost:8080 -- sleep 10
echo "Upload Material to Galaxy"
python /app/upload_material.py
echo "Kill Galaxy process"
kill $GALAXY_PID
