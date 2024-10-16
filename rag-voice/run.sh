cd Strathweb.Samples.Realtime.Rag
ffplay -f s16le -ar 24000 user-question.pcm -autoexit -nodisp
dotnet run
ffplay -f s16le -ar 24000 assistant-response.pcm -autoexit -nodisp