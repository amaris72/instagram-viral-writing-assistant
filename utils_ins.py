from prompt_template_ins import system_template_text, user_template_text
from langchain_openai import ChatOpenAI
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import ChatPromptTemplate
from ins_model import Instagram

# import os


def generate_instagram(theme, openai_api_key):
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_template_text),
            ("user", user_template_text)
        ]
    )

    model = ChatOpenAI(model="gpt-3.5-turbo",
                       openai_api_key="Your_Openai_Api_Key_here",
                       openai_api_base="https://api.aigc369.com/v1")

    output_parser = PydanticOutputParser(pydantic_object= Instagram)

    chain = prompt | model | output_parser

    result = chain.invoke({
        "parser_instructions": output_parser.get_format_instructions(),
        "theme": theme
    })

    return result

# print(generate_instagram("Makeup", os.getenv("OPENAI_API_KEY")))


