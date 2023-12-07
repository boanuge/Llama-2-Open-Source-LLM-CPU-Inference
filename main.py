import timeit
import argparse
from src.utils import setup_dbqa


if __name__ == "__main__":

    # Setup DBQA
    start = timeit.default_timer()
    dbqa = setup_dbqa()
    #response = dbqa({'query': 'How much is the minimum guarantee payable by adidas?'})
    #response = dbqa({'query': '예수님이 누구신가요?'}) # 한국어 인식은 잘 안되는듯함
    #response = dbqa({'query': 'Who is Jesus?'})
    response = dbqa({'query': 'Who is Holy Spirit?'})
    end = timeit.default_timer()

    print(f'\nAnswer: {response["result"]}')
    print('='*50)

    # Process source documents
    source_docs = response['source_documents']
    for i, doc in enumerate(source_docs):
        print(f'\nSource Document {i+1}\n')
        print(f'Source Text: {doc.page_content}')
        print(f'Document Name: {doc.metadata["source"]}\n')
        #print(f'Page Number: {doc.metadata["page"]}\n')
        print('='* 60)

    print(f"Time to retrieve response: {end - start}")
