mkdir -p pytest
/usr/bin/protoc --python_out=pytest mavlink.proto
/usr/bin/protoc --encode=Envelope mavlink.proto <hbtest.txt >hbtest.bin
/usr/bin/protoc --encode=Envelope mavlink.proto <gpsshorttest.txt >gpsshorttest.bin
