#!/bin/bash

cd Strathweb.Samples.Realtime.Rag

ffplay -f s16le -ar 24000 user-question.pcm -autoexit -nodisp 

mkfifo assistant-response.pcm

ffplay -f s16le -ar 24000 assistant-response.pcm -autoexit -nodisp > /dev/null 2>&1 &
FFPLAY_PID=$!
dotnet bin/Release/net9.0/Strathweb.Samples.Realtime.Rag.dll
wait $FFPLAY_PID

rm assistant-response.pcm