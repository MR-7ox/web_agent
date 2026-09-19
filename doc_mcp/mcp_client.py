import asyncio

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def main():

    server_params = StdioServerParameters(
        command="python",
        args=["doc_mcp.py"],
    )

    async with stdio_client(server_params) as (read, write):

        async with ClientSession(read, write) as session:

            # Start MCP session
            await session.initialize()

            # Get available tools
            result = await session.list_tools()

            for tool in result.tools:
                print(tool.name)

            result  = await session.call_tools
            {

                   "read_document",
                {"doc_id": "report.pdf"}
            }
            print(result)


asyncio.run(main())