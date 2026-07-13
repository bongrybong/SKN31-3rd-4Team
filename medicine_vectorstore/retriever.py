from vectorstore import load_vectorstore

vectorstore = load_vectorstore()

def retriever(query, ingredient_code, section=None, k=3):

    filter_dict = {
        "ingredient_code": ingredient_code
    }

    if section:
        filter_dict["section"] = section

    result = vectorstore.similarity_search(
        query=query,
        k=k,
        filter=filter_dict
    )

    return result