# Related Work based CrewAI

This project is designed to automatically process PDF papers, extract relevant metadata, abstract, key findings, and
reference lists, and generate a structured profile for each paper. It leverages an agent-based architecture to interact
with the PDF extraction tool and organize the extracted data. The system is built with the goal of streamlining the
process of generating a **Related Work** section for academic papers.

## Project Overview

The goal of this system is to support an intelligent literature review process by automating the extraction of key
information from academic papers, such as:

- Paper metadata (title, authors, publication year)
- Abstract and key findings
- Reference lists and citations

By processing these PDFs and storing the extracted data in a structured format (e.g., JSON), researchers can quickly
build a comprehensive literature review that highlights important papers, trends, and citations in their field of study.

## Features

- **Extracts paper metadata**: Extracts the title, authors, and publication year from PDF papers.
- **Retrieves abstract and key findings**: Extracts the abstract and identifies key findings from each paper.
- **Extracts reference lists and citations**: Identifies and extracts reference lists and citations mentioned in the
  papers.
- **Generates a structured JSON profile**: For each processed paper, a structured JSON profile is created.
- **Supports easy integration with external PDF extraction tools**: Easily integrates with any external tool for PDF
  processing.

## Missions to Complete

The system supports a range of missions that can be executed to further enhance the literature review process:

1. **Add More Papers to Review**: Automate the process of discovering additional papers that should be included in the
   literature review.
2. **Generate a Related Work Summary**: Create a summary of the related work section based on the processed papers. This
   agent will use the extracted metadata, abstracts, and key findings to generate a coherent paragraph summarizing the
   state-of-the-art in the field.

Bonus:
1. **Prompt Engineering**: Generate better prompts for the agents and tasks- this will help improve the quality of the extracted information and the generated summaries.

2. **Split the Method Agent into Mini Missions**: Decompose the original method agent into smaller, more manageable
   missions. This will allow each mini-agent to focus on one aspect of the paper extraction process (e.g., one agent for
   extracting metadata, another for extracting references), increasing modularity and scalability.

3. **Get the User's Area of Focus**: Collect information about the user's specific area of interest to filter out
   irrelevant papers. This step will ensure that only relevant papers are included in the review.

4. **Find Common Citations and Recommend**: The system will analyze the citations within the reviewed papers and find
   common references that the user might not have initially provided. These papers will be recommended based on their
   relevance to the user's area of focus.
5. **Any other interesting idea**

Please start by implementing the first 2 missions, and then proceed with the bonus missions as you see fit.
I encourage you to visit CrewAI for more information on the architecture- https://docs.crewai.com/en/learn/overview.
## Requirements

To run this project, make sure you have the following dependencies installed:

- Python 3.10 - 3.13
- Required Python libraries can be found in the `requirements.txt` file.

You can install the necessary libraries using `pip`:

```bash
pip install -r requirements.txt


