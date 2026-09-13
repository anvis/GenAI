from docx import Document
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT

output_path = "GenAI-Learning-Narrative.docx"

doc = Document()

def add_heading(text, level=1):
    doc.add_heading(text, level=level)


def add_paragraph(text, style=None, bold=False, italic=False):
    para = doc.add_paragraph(text)
    if style:
        para.style = style
    for run in para.runs:
        if bold:
            run.bold = True
        if italic:
            run.italic = True
    return para


def add_code_block(code):
    para = doc.add_paragraph()
    run = para.add_run(code)
    run.font.name = "Courier New"
    run.font.size = Pt(9)
    run.font.color.rgb = RGBColor(0, 0, 139)
    return para

def add_separator():
    doc.add_paragraph("-" * 80)


add_heading("The Complete AI Journey", level=0)
add_heading("From Mathematical Foundations to Generative Systems", level=2)
add_paragraph(
    "A comprehensive narrative of how artificial intelligence works, built from first principles to production-ready systems."
)
add_paragraph("This document tells the story of AI by connecting 140+ topics across mathematics, machine learning, deep learning, and generative AI.", italic=True)

add_heading("1. The Foundation: AI, GenAI, and the Math Behind It", level=1)
add_paragraph("Q: What is the difference between AI, GenAI, and AGI?")
add_paragraph(
    "A: Artificial intelligence is the broad field of machines making decisions or predictions from data. "
    "Generative AI is a subset that creates new content such as text, images, audio, and code. "
    "AGI is a theoretical future system with human-level, general problem-solving ability."
)

add_paragraph("Q: Why do vectors, matrices, and tensors matter in machine learning?")
add_paragraph(
    "A: Vectors represent features, matrices organize data and weights, and tensors extend this to higher dimensions. "
    "These structures let models perform fast algebraic operations, encode text embeddings, and carry image or batch data through neural networks."
)

add_paragraph("Q: How do covariance and correlation differ?")
add_paragraph(
    "A: Covariance shows whether two variables move together, but its scale depends on the data units. "
    "Correlation standardizes that relationship to a range from -1 to +1, making strength and direction easy to compare."
)
add_paragraph("Example:")
add_code_block(
"""# Covariance vs correlation example
import numpy as np
x = np.array([1, 2, 3, 4])
y = np.array([2, 4, 6, 8])
print(np.cov(x, y)[0, 1])
print(np.corrcoef(x, y)[0, 1])"""
)

add_heading("2. Machine Learning Concepts", level=1)
add_paragraph("Q: What is the bias-variance tradeoff?")
add_paragraph(
    "A: Bias occurs when a model is too simple and underfits the data; variance occurs when it is too sensitive and overfits. "
    "The goal is a model that generalizes well, not one that memorizes training noise or ignores real patterns."
)

add_paragraph("Q: What is gradient descent and why is backpropagation important?")
add_paragraph(
    "A: Gradient descent is the optimization process of taking small steps down a loss surface toward lower error. "
    "Backpropagation computes how much each network weight contributed to error so the model can update weights correctly."
)
add_code_block(
"""# Pseudo-code for the learning loop
for epoch in range(epochs):
    predictions = model.forward(inputs)
    loss = loss_fn(predictions, labels)
    gradients = model.backward(loss)
    model.update_weights(gradients, learning_rate)"""
)

add_heading("3. Deep Learning and Generative Models", level=1)
add_paragraph("Q: What is a perceptron and how does it connect to modern neural networks?")
add_paragraph(
    "A: A perceptron is a binary classifier that multiplies inputs by weights, sums them, and applies an activation threshold. "
    "Stacked together, perceptrons form multi-layer networks that can solve more complex, non-linear problems."
)

add_paragraph("Q: What are GANs, VAEs, and diffusion models?")
add_paragraph(
    "A: GANs use two networks (generator and discriminator) to create realistic data. "
    "VAEs encode inputs into a latent space and decode them back, useful for structured generation. "
    "Diffusion models generate samples by reversing a noise process, now common in image creation."
)

add_heading("4. Transformers, LLMs, and the GenAI Stack", level=1)
add_paragraph("Q: What makes transformers and LLMs central to GenAI?")
add_paragraph(
    "A: Transformers use attention to weigh all input tokens relative to each other, making them ideal for language understanding and generation. "
    "Large language models are transformer-based systems pre-trained on massive text corpora and fine-tuned for tasks like chat, summarization, and code generation."
)

add_paragraph("Q: What is pretraining, fine-tuning, and RLHF?")
add_paragraph(
    "A: Pretraining teaches a base model general language patterns by predicting tokens. "
    "Fine-tuning adapts that model to a specific task or domain. "
    "Reinforcement learning from human feedback aligns outputs with human preferences and safety goals."
)

add_heading("5. Practical GenAI Systems: Embeddings, RAG, and LangChain", level=1)
add_paragraph("Q: Why do vector databases matter for GenAI?")
add_paragraph(
    "A: Vector databases store embeddings so semantic search can retrieve the most relevant documents based on meaning, not keyword matches. "
    "This is the foundation of RAG (retrieval-augmented generation), where LLMs combine retrieved context with generative answers."
)

add_paragraph("Q: What is LangChain and what are prompt templates, chains, and agents?")
add_paragraph(
    "A: LangChain is a framework that organizes LLM interactions into reusable building blocks. Prompt templates create dynamic instructions, chains connect multiple steps, and agents decide which tools to use and when."
)
add_code_block(
"""from langchain_core.prompts import PromptTemplate
from langchain_core.llms import OpenAI
from langchain.chains import LLMChain

prompt = PromptTemplate.from_template('Tell me a joke about {topic}')
llm = OpenAI(model='gpt-4')
chain = LLMChain(llm=llm, prompt=prompt)
print(chain.invoke({'topic': 'cats'}))"""
)

add_paragraph("Q: What does agent orchestration look like?")
add_paragraph(
    "A: Agent orchestration coordinates specialized agents and tools so they work like a team. "
    "One agent may search data, another summarizes it, and a manager decides which agent to call based on the user query."
)

add_heading("6. Interview-Ready Takeaways", level=1)
add_paragraph("Q: What are the strongest points to mention in an AI interview?")
add_paragraph(
    "A: Know the learning journey: math foundations, bias-variance tradeoff, optimization via gradient descent, neural architectures, and how modern GenAI combines transformers with retrieval and agent orchestration. "
    "Also mention practical tools like LangChain, ChromaDB, and the value of prompt design and memory in building real applications."
)

add_paragraph("Q: How do these topics connect?")
add_paragraph(
    "A: Basic math delivers the language of models. Machine learning introduces training and generalization. Deep learning adds expressive networks and generative models. "
    "Transformers and embeddings turn that foundation into GenAI applications, while vector retrieval and agents make those applications useful in the real world."
)

add_heading("Quick Links to the Repository Topics", level=1)
add_paragraph("- Basics: linear algebra, covariance/correlation, bias vs variance")
add_paragraph("- ML: supervised/unsupervised learning, underfitting/overfitting, gradient descent")
add_paragraph("- Deep Learning: perceptron, MLP, GANs, VAEs, diffusion")
add_paragraph("- GenAI: transformers, LLMs, fine-tuning, RLHF, LangChain, RAG, ChromaDB, agent orchestration")

add_heading("How to Use This Sheet", level=1)
add_paragraph(
    "Read it as a learning path. Start with the first section, then follow the connections between topics. "
    "Use the code snippets as practical anchors that show how repository concepts move from idea to implementation."
)

add_paragraph("Generated from the repository’s learning journey and organized for interview preparation.")

doc.save(output_path)
print(f'Generated {output_path}')
