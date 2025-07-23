import os
from textwrap import dedent
from crewai import Crew, Process
from dotenv import load_dotenv

from agents import CustomAgents
from tasks import CustomTasks

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")


class RelatedWorkCrew:
    def __init__(self):
        pass

    def run(self):
        agents = CustomAgents()
        tasks = CustomTasks()

        # Define the PDF path for each paper
        inputs_papers = ['paper1.pdf']
        results = []
        for pdf_path in inputs_papers:
            pdf_path = os.path.join('Data', pdf_path)

            # Initialize the agent and task for this specific paper
            pdf_processor = agents.pdf_agent(paper_path=pdf_path)
            method_agent = agents.method_agent(paper_path=pdf_path)
            pdf_processing_task = tasks.pdf_summary_task(pdf_processor, paper_path=pdf_path)
            method_analysis_task = tasks.method_analysis_task(method_agent, paper_path=pdf_path,
                                                              context_task=pdf_processing_task)

            analysis_per_paper_crew = Crew(
                agents=[pdf_processor, method_agent],
                tasks=[pdf_processing_task, method_analysis_task],
                process=Process.sequential,
                verbose=True,
            )

            result = analysis_per_paper_crew.kickoff()
            results.append(result)

        return results


def main():
    print('### Welcome to the Related Work Crew! ###')
    print("-------------------------------------------")
    crew = RelatedWorkCrew()
    result = crew.run()

    print("### Result ###")
    print("-------------------------------------------")
    print(result)


if __name__ == "__main__":
    main()
