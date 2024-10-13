# 2024-ndcporto-demos

## Demos

* Basic RAG with BYOD (shop)
  * “i need a football” (keyword)
  * “anything featuring bird pattern” (vector)

* Promptflow RAG:
  * search for “i need something Miami themed"
  * run the orchestration:

```
pf run create --flow . --data data/sample.jsonl --column-mapping user_id='${data.user_id}'  --column-mapping question='${data.question}' --column-mapping chat_history='${data.chat_history}' --stream
```

  * and visualize - notice how the second flow resolves the search query correctly

```
pf run visualize -n NAME
```

* Promptflow - Chat with images/Vision (shop)
  * search for “do you have anything in this style” + Flamingo - correct response (Flamingo football)
  * search for “do you have a uniform that matches this football” + Flamingo football - correct response (Flamingo uniform)

* Bench:
  * Promptflow - Data flow (arxiv)