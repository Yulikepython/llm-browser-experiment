import asyncio
from dotenv import load_dotenv
load_dotenv()

import sys
from langchain_openai import ChatOpenAI
from browser_use import Agent
from result_handler import process_result

# プロンプト管理用
import prompt_manager

MODEL = "gpt-4o"

async def main():
    # コマンドライン or 環境変数から promptファイル名を取得
    prompt_name = prompt_manager.get_prompt_from_env_or_arg()

    if not prompt_name:
        # 未指定ならサンプルを一覧表示して終了させる or デフォルト設定
        print("Usage: python main.py <prompt_name>")
        print("Examples:")
        print("  python main.py sample_prompt1")
        print("  python main.py sample_prompt2")
        print("  python main.py personal_prompt1  (in my_prompts/)")
        sys.exit(1)

    # 該当のtask_promptをロード
    try:
        task_prompt = prompt_manager.load_prompt_by_name(prompt_name)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except ImportError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except AttributeError as e:
        print(f"Error: {e}")
        sys.exit(1)

    # エージェントを実行
    agent = Agent(
        task=task_prompt,
        llm=ChatOpenAI(model=MODEL),
    )
    result_history = await agent.run()

    # 実行結果をファイル出力
    process_result(
        task_prompt=task_prompt,
        result_history=result_history,
        out_dir="outputs",
        extension="md",
    )

if __name__ == "__main__":
    asyncio.run(main())
