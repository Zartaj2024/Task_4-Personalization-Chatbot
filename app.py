
import chainlit as cl
from agents import Runner
from agents.items import ToolCallItem, ToolCallOutputItem
from agent import agent
import logging

@cl.on_chat_start
async def on_chat_start():
    cl.user_session.set("agent", agent)
    await cl.Message(content="Hello, how can I assist you today?").send()

@cl.on_message
async def on_message(message: cl.Message):
    agent = cl.user_session.get("agent")
    try:
        await cl.Message(content="Processing your request...").send()
        result = await Runner.run(agent, input=message.content)
        
        # Use result.new_items to access the steps
        if result.new_items:
            for step in result.new_items:
                if isinstance(step, ToolCallItem):
                    # Access attributes from raw_item for tool calls
                    await cl.Message(content=f"Tool call: {step.raw_item.name} with args {step.raw_item.arguments}").send()
                if isinstance(step, ToolCallOutputItem):
                    # Access the output attribute for tool outputs
                    await cl.Message(content=f"Tool output: {step.output}").send()
        
        if result.final_output:
            await cl.Message(content=result.final_output).send()
        else:
            await cl.Message(content="I was not able to produce a response. Please check your API key and model configuration.").send()

    except Exception as e:
        logging.error(f"An error occurred: {e}", exc_info=True)
        await cl.Message(content=f"An error occurred: {e}").send()
