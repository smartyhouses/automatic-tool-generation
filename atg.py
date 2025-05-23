import uuid
from langgraph.checkpoint.memory import MemorySaver
from core.graph import builder


class AgentBuilder:
    def __init__(self,
                 planner_provider="openai",
                 planner_model="o3-mini",
                 writer_provider="openai",
                 writer_model="gpt-4.1-nano",
                 file_type="CSV",
                 index4file="true",
                 breadth=2,
                 max_tokens=32768 ,):
        # Configurable parameters
        self.planner_provider = planner_provider
        self.planner_model = planner_model
        self.writer_provider = writer_provider
        self.writer_model = writer_model
        self.file_type = file_type
        self.index4file = index4file
        self.breadth = breadth
        self.max_tokens = max_tokens

        # Internal state
        self.memory = MemorySaver()
        self.graph = builder.compile(checkpointer=self.memory)

        # Generate default thread config
        self.thread = {
            "configurable": {
                "thread_id": str(uuid.uuid4()),
                "planner_provider": self.planner_provider,
                "planner_model": self.planner_model,
                "writer_provider": self.writer_provider,
                "writer_model": self.writer_model,
                "file_type": self.file_type,
                "index4file": self.index4file,
                "breadth": self.breadth,
                "max_tokens": self.max_tokens,
            }
        }

    async def run(self, file_path: str):
        """
        Run the graph asynchronously for a given input file.
        """
        event = {"orig_file_path": file_path}
        results = []

        async for s in self.graph.astream(event, self.thread, stream_mode="updates"):
            # print("================================")
            # print(s)
            print("running...")
            results.append(s)

        return results[-1]['response2file']["tool_save_path"]

if __name__ == "__main__":
    import asyncio
    from dotenv import load_dotenv

    load_dotenv()

    file_path = ""

    agent = AgentBuilder()
    results = asyncio.run(agent.run(file_path))
