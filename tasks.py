from crewai import Task
from textwrap import dedent


class CustomTasks:

    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you $10,000 tip!"

    def pdf_summary_task(self, agent, paper_path):
        return Task(
            description=dedent(f"""
                        Thoroughly analyze the research paper located at: {paper_path}
                
                        **Your mission is to extract and structure the following information:**
                
                        1. **Document Metadata:**
                           - Complete paper title (exact as written, written at the top of the first page)
                           - All author names and affiliations (written under the title)
                           - Publication year and venue (journal/conference)
                
                        2. **Content Structure Analysis:**
                           - Abstract content (complete text)
                           - Key research questions or hypotheses
                           - Main contributions claimed by authors
                
                        3. **Research Content Summary:**
                           - Primary research domain/field
                           - Problem being addressed
                           - Proposed solution or approach (high-level)
                           - Key findings and results
                           - Main conclusions
                
                        4. **Reference and Citation Analysis:**
                           - Extract first 10 most relevant references from the relative work section
                
                        5. **Technical Assessment:**
                           - Identify if paper is theoretical, empirical, or mixed
                           - Datasets mentioned (if any)
                            - Code availability status (yes/no/unclear)
                
                        **Instructions:**
                        - Use the PDFSearchTool to thoroughly search through the paper
                        - Pay special attention to abstract, introduction, and conclusion sections
                        - Look for explicit statements of contributions and novelty
                        - Be precise with author names and publication details
                        - If information is unclear or missing, clearly state so
                
                        {self.__tip_section()}
                        """),

            agent=agent,
            expected_output=dedent(f"""
                            A comprehensive JSON structure containing:
                
                            {{
                                "paper_metadata": {{
                                    "title": "Complete paper title",
                                    "authors": ["Author 1", "Author 2", ...],
                                    "publication_year": "YYYY",
                                    "venue": "Journal/Conference name",
                                }},
                                "content_analysis": {{
                                    "abstract": "Complete abstract text",
                                    "research_domain": "Primary field/domain",
                                    "problem_addressed": "What problem does this solve",
                                    "proposed_approach": "High-level approach description",
                                    "key_findings": ["Finding 1", "Finding 2", ...],
                                    "main_contributions": ["Contribution 1", "Contribution 2", ...],
                                }},
                                "references_info": {{
                                    "key_references": ["Ref 1", "Ref 2", ...],
                                }},
                                "technical_details": {{
                                    "paper_type": "theoretical/empirical/mixed",
                                    "datasets_mentioned": ["Dataset 1", "Dataset 2", ...],
                                    "code_availability": "yes/no/unclear",
                                }}
                            }}
                            """),
            output_file=f'processed_paper_{paper_path}.json'
        )

    # Task 2: Deep Method Analysis
    def method_analysis_task(self, agent, paper_path, context_task):
        return Task(
            description=dedent(f"""
                        Conduct a comprehensive methodology analysis of the paper: {paper_path}
                
                        Using the extracted PDF content from the previous task, perform deep analysis of:
                
                        **1. Core Methodology Analysis:**
                        - What is the primary research methodology/approach used?
                        - Is it a novel method or extension of existing work?
                        - What theoretical framework does it build upon?
                        - What are the key algorithmic or technical components?
                
                        **2. Technical Innovation Assessment:**
                        - What specific innovations does this paper introduce?
                        - How does it differ from existing approaches?
                        - What are the novel technical contributions?
                        - Are there any new algorithms, models, or techniques?
                
                        **3. Experimental Design Analysis:**
                        - What experimental setup is used?
                        - What datasets or benchmarks are employed?
                        - What evaluation metrics are used?
                        - How are baselines chosen and compared?
                        - What validation methods are employed?
                
                        **4. Results and Performance Analysis:**
                        - What are the key quantitative results?
                        - How does performance compare to existing methods?
                        - What improvements are demonstrated?
                        - Are results statistically significant?
                
                        **5. Critical Analysis:**
                        - What limitations does the paper acknowledge?
                        - What are potential weaknesses or drawbacks?
                        - What assumptions are made?
                        - What future work is suggested?
                        - What questions remain unresolved?
                
                        **6. Methodological Context:**
                        - How does this work fit into the broader research landscape?
                        - What previous work does it build upon?
                        - What research gap does it address?
                        - How might it influence future research?
                
                        **Analysis Instructions:**
                        - Focus on the methodology and technical approach sections
                        - Look for mathematical formulations, algorithms, and technical details
                        - Identify both strengths and weaknesses objectively
                        - Consider reproducibility and practical applicability
                
                        {self.__tip_section()}
                        """),

            agent=agent,
            context=[context_task],
            expected_output=dedent(f"""
                            A detailed methodology analysis in JSON format:
                            {{
                                "methodology_overview": {{
                                    "primary_approach": "Main methodological approach",
                                    "research_type": "theoretical/empirical/experimental/survey",
                                    "novelty_level": "completely new/incremental improvement/application",
                                    "theoretical_foundation": "What theories/frameworks it builds on"
                                }},
                                "technical_contributions": {{
                                    "key_innovations": ["Innovation 1", "Innovation 2", ...],
                                    "algorithms_introduced": ["Algorithm 1", "Algorithm 2", ...],
                                    "technical_improvements": ["Improvement 1", "Improvement 2", ...],
                                    "theoretical_advances": ["Advance 1", "Advance 2", ...]
                                }},
                                "experimental_setup": {{
                                    "datasets_used": ["Dataset 1", "Dataset 2", ...],
                                    "evaluation_metrics": ["Metric 1", "Metric 2", ...],
                                    "baseline_methods": ["Baseline 1", "Baseline 2", ...],
                                    "experimental_design": "Description of experimental approach"
                                }},
                                "performance_analysis": {{
                                    "key_results": ["Result 1", "Result 2", ...],
                                    "performance_improvements": {{"metric": "improvement"}},
                                    "statistical_significance": "yes/no/unclear",
                                    "result_interpretation": "How to interpret the results"
                                }},
                                "critical_assessment": {{
                                    "acknowledged_limitations": ["Limitation 1", "Limitation 2", ...],
                                    "potential_weaknesses": ["Weakness 1", "Weakness 2", ...],
                                    "assumptions_made": ["Assumption 1", "Assumption 2", ...],
                                    "reproducibility": "high/medium/low/unclear"
                                }},
                                "research_context": {{
                                    "builds_upon": ["Previous work 1", "Previous work 2", ...],
                                    "addresses_gap": "What research gap is addressed",
                                    "potential_impact": "Potential impact on the field",
                                    "future_directions": ["Direction 1", "Direction 2", ...]
                                }}
                            }}
                            """),
            output_file=f'method_analysis_{paper_path}.json'
        )
    #
    # # Task 3: Relationship Mapping
    # def relationship_mapping(self,agent):
    #     return Task(
    #         description="""
    #                 Analyze all papers together to discover relationships:
    #                 1. Methodological similarities and differences
    #                 2. Papers that cite or build upon each other
    #                 3. Complementary vs competing approaches
    #                 4. Evolution of techniques across papers
    #                 5. Thematic groupings and clusters
    #                 6. Consensus areas and conflicting findings
    #                 7. Gaps in methodology coverage
    #
    #                 Create a comprehensive relationship map between all papers.
    #                 """,
    #         agent=agent,
    #         context=[method_analysis_task],
    #         expected_output="""
    #                 - Relationship matrix between papers
    #                 - Thematic clusters and groupings
    #                 - Methodological family trees
    #                 - Consensus vs conflict areas
    #                 - Research gap identification"""
    #     )
    #
    # # Task 4: Related Work Generation
    # def summary_task(self,agent):
    #     return Task(
    #         description="""
    #                 Using all previous analysis, generate a comprehensive related work section:
    #                 1. Create logical thematic organization
    #                 2. Write introduction to the research area
    #                 3. Discuss each methodological cluster with supporting papers
    #                 4. Compare and contrast different approaches
    #                 5. Highlight evolution of techniques
    #                 6. Identify consensus and disagreements
    #                 7. Point out research gaps and opportunities
    #                 8. Ensure proper academic tone and citations
    #                 9. Create smooth transitions between sections
    #
    #                 Produce a publication-ready related work section.
    #                 """,
    #         agent=agent,
    #         context=[relationship_mapping_task],
    #         expected_output="""Complete related work section including:
    #                 - Structured thematic organization
    #                 - Proper academic writing style
    #                 - Comprehensive paper coverage
    #                 - Relationship discussions
    #                 - Research gap analysis
    #                 - Proper citations throughout"""
    #     )
