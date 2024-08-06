from langchain_anthropic import ChatAnthropic
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from retry import retry
import json
import config as CONFIG
import os

class LLMClient:
    """
    This class is used to invoke the LLMs
    """

    def __init__(self, temperature=0, request_timeout=60):

        self.openai_chat_llm = ChatOpenAI(model_name=CONFIG.OPENAI_CHAT_MODEL,
                                          temperature=temperature,
                                          max_retries=CONFIG.OPENAI_RETRY_LIMIT,
                                          request_timeout=request_timeout)

        self.openai_gpt3_5_llm = ChatOpenAI(model_name=CONFIG.OPENAI_GPT3_5_MODEL,
                                            temperature=temperature,
                                            max_retries=CONFIG.OPENAI_RETRY_LIMIT,
                                            request_timeout=request_timeout)
        
        self.openai_gpt3_5_16k_llm = ChatOpenAI(model_name=CONFIG.OPENAI_GPT_16K_MODEL,
                                            temperature=temperature,
                                            max_retries=CONFIG.OPENAI_RETRY_LIMIT,
                                            request_timeout=request_timeout)
        
        self.openai_gpt_4o_llm = ChatOpenAI(model_name=CONFIG.OPENAI_GPT_4O_MODEL,
                                            temperature=temperature,
                                            max_retries=CONFIG.OPENAI_RETRY_LIMIT,
                                            request_timeout=request_timeout)


        self.anthropic_llm_2 = ChatAnthropic(model=CONFIG.ANTHROPIC_MODEL, temperature=temperature)
        
        self.anthropic_llm_sonnet = ChatAnthropic(model=CONFIG.ANTHROPIC_SONNET_MODEL, temperature=temperature)
        
        self.anthropic_llm_haiku = ChatAnthropic(model=CONFIG.ANTHROPIC_HAIKU_MODEL, temperature=temperature)
        
        self.anthropic_llm_sonnet_3_5 = ChatAnthropic(model=CONFIG.ANTHROPIC_SONNET_3_5_MODEL, temperature=temperature)
    
    def invoke(self, llm_family, model, output_token_count, user_prompt_template, chain_args, system_prompt_template = None):
        """
        This method is used to invoke the LLMs
        """
        if system_prompt_template:
            complete_prompt = ChatPromptTemplate.from_messages(
                [("system", system_prompt_template) , ("human", user_prompt_template)])
        else:
            complete_prompt = ChatPromptTemplate.from_messages([("human", user_prompt_template)])

        if llm_family == CONFIG.LLMFamily.OPEN_AI.name:
            if model == CONFIG.OPENAI_CHAT_MODEL:
                self.openai_chat_llm.max_tokens = output_token_count
                language_chain = complete_prompt | self.openai_chat_llm
            elif model == CONFIG.OPENAI_GPT3_5_MODEL:
                self.openai_gpt3_5_llm.max_tokens = output_token_count
                language_chain = complete_prompt | self.openai_gpt3_5_llm
            elif model == CONFIG.OPENAI_GPT_16K_MODEL:
                self.openai_gpt3_5_16k_llm.max_tokens = output_token_count
                language_chain = complete_prompt | self.openai_gpt3_5_16k_llm
            elif model ==  CONFIG.OPENAI_GPT_4O_MODEL:
                self.openai_gpt_4o_llm.max_tokens = output_token_count
                language_chain = complete_prompt | self.openai_gpt_4o_llm
            else:
                raise Exception("invalid model name passed for openAI family")
        else:
            if model == CONFIG.ANTHROPIC_MODEL:
                self.anthropic_llm_2.max_tokens = output_token_count
                language_chain = complete_prompt | self.anthropic_llm_2
            elif model == CONFIG.ANTHROPIC_SONNET_MODEL:
                language_chain = complete_prompt | self.anthropic_llm_sonnet
            elif model == CONFIG.ANTHROPIC_SONNET_3_5_MODEL:
                language_chain = complete_prompt | self.anthropic_llm_sonnet_3_5
            else:
                language_chain = complete_prompt | self.anthropic_llm_haiku

        output = language_chain.invoke(chain_args)
        return output.content