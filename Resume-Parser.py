import openai

def parse_resume_to_json(resume_text):
    prompt = f"""
    Parse the following resume and output the content in JSON format. The resume sections include "Contact Information", "Summary", "Experience", "Education", "Skills", and "Certifications". Each section should be a key in the JSON object, with the corresponding content as values. Here's the resume:

    {resume_text}

    Output format:
    {{
      "Contact Information": {{
        "Name": "",
        "Address": "",
        "Phone": "",
        "Email": "",
        "LinkedIn": ""
      }},
      "Summary": "",
      "Experience": [
        {{
          "Job Title": "",
          "Company": "",
          "Location": "",
          "Start Date": "",
          "End Date": "",
          "Responsibilities": ""
        }}
      ],
      "Education": [
        {{
          "Degree": "",
          "Institution": "",
          "Location": "",
          "Start Date": "",
          "End Date": ""
        }}
      ],
      "Skills": [],
      "Certifications": []
    }}
    """

    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=prompt,
      max_tokens=1500
    )

    return response.choices[0].text.strip()

# Example usage
resume_text = """
John Doe
123 Main St, Anytown, USA
(123) 456-7890
john.doe@example.com
linkedin.com/in/johndoe

Summary
Experienced software engineer with expertise in AI and machine learning.

Experience
Software Development Engineer at TechCorp
Anytown, USA
June 2020 - Present
- Developed AI models to improve user experience
- Collaborated with cross-functional teams

Education
Bachelor of Science in Computer Science
University of Anytown
Anytown, USA
September 2016 - May 2020

Skills
Python, Java, Machine Learning, AI, Data Analysis

Certifications
Certified Kubernetes Administrator
"""

parsed_resume = parse_resume_to_json(resume_text)
print(parsed_resume)
