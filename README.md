================================================================================<br>
Issue Solution : import langchain TypeError: issubclass() arg 1 must be a class<br>
================================================================================<br>
...<br>
  File "pydantic\main.py", line 198, in pydantic.main.ModelMetaclass.__new__<br>
  File "pydantic\fields.py", line 506, in pydantic.fields.ModelField.infer<br>
  File "pydantic\fields.py", line 436, in pydantic.fields.ModelField.__init__<br>
  File "pydantic\fields.py", line 552, in pydantic.fields.ModelField.prepare<br>
  File "pydantic\fields.py", line 663, in pydantic.fields.ModelField._type_analysis<br>
  File "pydantic\fields.py", line 808, in pydantic.fields.ModelField._create_sub_type<br>
  File "pydantic\fields.py", line 436, in pydantic.fields.ModelField.__init__<br>
  File "pydantic\fields.py", line 552, in pydantic.fields.ModelField.prepare<br>
  File "pydantic\fields.py", line 668, in pydantic.fields.ModelField._type_analysis<br>
  File "C:\ProgramData\Anaconda3\lib\typing.py", line 852, in __subclasscheck__<br>
    return issubclass(cls, self.__origin__)<br>
TypeError: issubclass() arg 1 must be a class<br>
PS C:\AI\ai_@_wwhss_alpha_version_orca2_13b><br>
<br>
First, try the following:<br>
(base) $ pip install typing-inspect==0.8.0 typing_extensions==4.5.0<br>
If above command is not resolve the issue, then:<br>
(base) $ pip install pydantic -U<br>
(base) $ pip install pydantic==1.10.11<br>
<br>
### @ https://www.youtube.com/watch?v=gdzeE6ys2nM

PS C:\AI\Llama-2-Open-Source-LLM-CPU-Inference_@_github.com> conda activate base <br>
PS C:\AI\Llama-2-Open-Source-LLM-CPU-Inference_@_github.com> python .\db_build.py <br>
PS C:\AI\Llama-2-Open-Source-LLM-CPU-Inference_@_github.com> python .\main.py <br>
<br>
## Answer: Jesus is the Christ, the Son of God.
==================================================<br>
Source Document 1 <br>
Source Text: Matthew 16:13 Now when Jesus had come into the parts of Caesarea Philippi, he said, questioning his disciples, Who do men say that the Son of man is?
Matthew 16:14 And they said, Some say, John the Baptist; some, Elijah; and others, Jeremiah, or one of the prophets.
Matthew 16:15 He says to them, But who do you say that I am?
Matthew 16:16 And Simon Peter made answer and said, You are the Christ, the Son of the living God. <br>
Document Name: data\data_5_bible_english_BBE.txt <br>
============================================================<br>
Source Document 2 <br>
Source Text: John 20:31 But these are recorded, so that you may have faith that Jesus is the Christ, the Son of God, and so that, having this faith you may have life in his name.
John 21:1 After these things Jesus let himself be seen again by the disciples at the sea of Tiberias; and it came about in this way.
John 21:2 Simon Peter, Thomas named Didymus, Nathanael of Cana in Galilee, the sons of Zebedee, and two others of his disciples were all together. <br>
Document Name: data\data_5_bible_english_BBE.txt <br>
============================================================<br>
Time to retrieve response: 52.476544000000004 <br>
PS C:\AI\Llama-2-Open-Source-LLM-CPU-Inference_@_github.com> <br>

<br>

# Running Llama 2 and other Open-Source LLMs on CPU Inference Locally for Document Q&A

### Clearly explained guide for running quantized open-source LLM applications on CPUs using LLama 2, C Transformers, GGML, and LangChain

**Step-by-step guide on TowardsDataScience**: https://towardsdatascience.com/running-llama-2-on-cpu-inference-for-document-q-a-3d636037a3d8
___
## Context
- Third-party commercial large language model (LLM) providers like OpenAI's GPT4 have democratized LLM use via simple API calls. 
- However, there are instances where teams would require self-managed or private model deployment for reasons like data privacy and residency rules.
- The proliferation of open-source LLMs has opened up a vast range of options for us, thus reducing our reliance on these third-party providers. 
- When we host open-source LLMs locally on-premise or in the cloud, the dedicated compute capacity becomes a key issue. While GPU instances may seem the obvious choice, the costs can easily skyrocket beyond budget.
- In this project, we will discover how to run quantized versions of open-source LLMs on local CPU inference for document question-and-answer (Q&A).
<br><br>
![Alt text](assets/diagram_flow.png)
___

## Quickstart
- Ensure you have downloaded the GGML binary file from https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML and placed it into the `models/` folder
- To start parsing user queries into the application, launch the terminal from the project directory and run the following command:
`poetry run python main.py "<user query>"`
- For example, `poetry run python main.py "What is the minimum guarantee payable by Adidas?"`
- Note: Omit the prepended `poetry run` if you are NOT using Poetry
<br><br>
![Alt text](assets/qa_output.png)
___
## Tools
- **LangChain**: Framework for developing applications powered by language models
- **C Transformers**: Python bindings for the Transformer models implemented in C/C++ using GGML library
- **FAISS**: Open-source library for efficient similarity search and clustering of dense vectors.
- **Sentence-Transformers (all-MiniLM-L6-v2)**: Open-source pre-trained transformer model for embedding text to a 384-dimensional dense vector space for tasks like clustering or semantic search.
- **Llama-2-7B-Chat**: Open-source fine-tuned Llama 2 model designed for chat dialogue. Leverages publicly available instruction datasets and over 1 million human annotations. 
- **Poetry**: Tool for dependency management and Python packaging

___
## Files and Content
- `/assets`: Images relevant to the project
- `/config`: Configuration files for LLM application
- `/data`: Dataset used for this project (i.e., Manchester United FC 2022 Annual Report - 177-page PDF document)
- `/models`: Binary file of GGML quantized LLM model (i.e., Llama-2-7B-Chat) 
- `/src`: Python codes of key components of LLM application, namely `llm.py`, `utils.py`, and `prompts.py`
- `/vectorstore`: FAISS vector store for documents
- `db_build.py`: Python script to ingest dataset and generate FAISS vector store
- `main.py`: Main Python script to launch the application and to pass user query via command line
- `pyproject.toml`: TOML file to specify which versions of the dependencies used (Poetry)
- `requirements.txt`: List of Python dependencies (and version)
___

## References
- https://github.com/marella/ctransformers
- https://huggingface.co/TheBloke
- https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML
- https://python.langchain.com/en/latest/integrations/ctransformers.html
- https://python.langchain.com/en/latest/modules/models/llms/integrations/ctransformers.html
- https://python.langchain.com/docs/ecosystem/integrations/ctransformers
- https://ggml.ai
- https://github.com/rustformers/llm/blob/main/crates/ggml/README.md
- https://www.mdpi.com/2189676
