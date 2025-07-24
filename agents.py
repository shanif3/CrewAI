from crewai import Agent
from langchain_openai import ChatOpenAI
from crewai_tools import PDFSearchTool
from textwrap import dedent


class CustomAgents:
    def __init__(self):
        self.OPENAIGPT4o = ChatOpenAI(model="gpt-4o")
        self.OPENAIGPT4 = ChatOpenAI(model="gpt-4")

    # Agent 1: PDF Processing
    def pdf_agent(self, paper_path):
        return Agent(
            role=dedent("Senior Academic PDF Analyst"),
            goal=dedent(f"Extract comprehensive academic content and metadata from the research paper: {paper_path}"),
            backstory=dedent(f"""
                    You are a highly skilled academic document analyst with expertise in 
                    processing research papers. You specialize in extracting structured information from 
                    academic PDFs, including metadata, content organization, and approaches used in the research.
                    Your current task is to thoroughly analyze the paper: '{paper_path}'
                    You have experience with:
                    - Academic paper structure and formatting
                    - Citation and reference extraction
                    - Metadata identification (authors, years)
                    - Content summarization and key finding identification
                    """),

            tools=[PDFSearchTool(paper_path)],
            verbose=True,
            llm=self.OPENAIGPT4o,
        )

    # Agent 2: Method Analysis
    def method_agent(self, paper_path):
        return Agent(
            role=dedent("Research Methodology Expert"),
            goal=dedent("Perform deep analysis of research methodologies, approaches, and contributions"),

            backstory=dedent("""
                    You are a research methodology expert with deep knowledge across 
                    multiple academic disciplines. You excel at:
            
                    - Identifying core research methodologies and approaches
                    - Analyzing algorithmic and technical innovations
                    - Understanding experimental design and evaluation
                    - Recognizing theoretical frameworks and contributions
                    - Extracting performance metrics and results
                    - Identifying limitations and future work directions
            
                    You have a PhD-level understanding of research methods and can quickly 
                    identify the key methodological contributions of any academic paper.
                    """),

            tools=[PDFSearchTool(paper_path)],
            verbose=True,
            llm=self.OPENAIGPT4o,
            reasoning=True,  # Enable strategic planning,
        )

