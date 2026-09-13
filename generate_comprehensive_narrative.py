from docx import Document
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT

output_path = "GenAI-Complete-Learning-Narrative.docx"
doc = Document()

def add_heading(text, level=1):
    doc.add_heading(text, level=level)

def add_paragraph(text, bold=False, italic=False):
    para = doc.add_paragraph(text)
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
    doc.add_paragraph("─" * 90)

# Title & Introduction
add_heading("The Complete AI Journey", level=0)
add_heading("From Mathematical Foundations to Generative Systems", level=2)
add_paragraph("A comprehensive narrative of how artificial intelligence works, built from first principles to production-ready systems.", italic=True)
add_paragraph("This guide connects 140+ topics across mathematics, machine learning, deep learning, and generative AI into one coherent story.", italic=True)

add_separator()

# PART 1: FOUNDATIONS
add_heading("Part 1: The Foundation — Mathematics That Powers AI", level=1)

add_paragraph(
    "Before you understand how AI works, you need to speak its language: mathematics. Every machine learning model, every neural network, "
    "every transformer is fundamentally a mathematical expression. The good news: the core concepts are elegant and intuitive. Let's start where it all begins."
)

add_heading("1.1 Vectors, Matrices, and the Building Blocks", level=2)
add_paragraph(
    "Imagine describing a house to someone: '3 bedrooms, 2 bathrooms, 2000 square feet.' These three numbers—[3, 2, 2000]—form a "
    "vector. In AI, everything starts as vectors. Images become vectors of pixel values. Text becomes vectors of numbers. Datasets become matrices "
    "(tables of vectors, where each row is a sample)."
)
add_paragraph(
    "But vectors don't just store data—they enable transformations. When a neural network processes your input, it multiplies your input vector by "
    "weight matrices, transforming it step by step. Linear algebra is the math of these transformations. Understand it, and you understand the backbone of AI."
)
add_code_block(
"""# Vectors and matrices in NumPy—the language of AI
import numpy as np

# A vector: house features
house = np.array([3, 2, 2000])

# A matrix: multiple houses
houses = np.array([
    [3, 2, 2000],   # House 1
    [4, 3, 3000],   # House 2
    [2, 1, 1500]    # House 3
])

# A neural network layer: dot product with weights
weights = np.array([100, 50, 1])
transformed = np.dot(houses, weights)  # [203050, 305000, 151500]"""
)

add_heading("1.2 Going Beyond Numbers: Relationships in Data", level=2)
add_paragraph(
    "Two huge questions in data: Do these variables move together? If so, how strongly? Covariance measures the first—whether two variables "
    "tend to increase or decrease together. But covariance has a problem: its scale depends on the units. Height in meters vs. feet gives "
    "different covariances even for the same relationship."
)
add_paragraph(
    "Correlation solves this by standardizing to a scale from -1 to +1. Correlation of +1 means perfect positive relationship; -1 means perfect "
    "negative; 0 means no linear relationship. In machine learning, when you select features or interpret relationships, you're using these concepts."
)
add_paragraph(
    "Example: College GPA vs study hours (likely strong positive correlation). Stock price vs competitor stock price (might be positive). "
    "Study time vs stress level (might be negative). These relationships guide which features matter and how well the model will generalize."
)

add_heading("1.3 Probability and Inference: Learning from Samples", level=2)
add_paragraph(
    "Real data is messy and limited. You never have the perfect dataset; you have a sample. Probability theory and inferential statistics "
    "let you make conclusions about the whole population from that sample. This is why hypothesis testing and p-values matter: they measure confidence."
)
add_paragraph(
    "When you train a machine learning model, you're making probabilistic statements about the invisible world: 'Given this training data, "
    "what's the probability my model will work on new data? How confident am I in this prediction? Does this difference matter, or is it random noise?' "
    "These questions require probability and statistics."
)

add_heading("1.4 Eigenvalues and Dimensionality: Finding the Signal", level=2)
add_paragraph(
    "Here's a profound idea: not all dimensions matter equally. An image dataset has millions of pixels, but most variation comes from a few "
    "factors (lighting, object size, angle). Eigenvalues and eigenvectors identify these dominant directions. Principal Component Analysis (PCA) uses "
    "this to compress data without losing essential information. You go from 10,000 dimensions to 50, yet most patterns remain."
)
add_paragraph(
    "This insight echoes through deep learning: neural networks learn to identify the most important features automatically, compressing high-dimensional "
    "data into low-dimensional representations. Embeddings are the modern version of this idea."
)

add_separator()

# PART 2: MACHINE LEARNING
add_heading("Part 2: Learning from Data — Classical Machine Learning", level=1)

add_paragraph(
    "Armed with math, we ask the central question: Can a computer learn patterns from data without being explicitly programmed for every scenario? "
    "The answer is yes. This is machine learning, and it's the engine behind countless real-world systems."
)

add_heading("2.1 The Learning Problem: Two Paths", level=2)
add_paragraph(
    "Machine learning splits into two philosophies. Supervised learning has labels: 'This email is spam.' 'This tumor is malignant.' 'This house costs $500k.' "
    "The model learns to map inputs to outputs by minimizing error on labeled examples. Email filters, medical diagnosis tools, and price prediction all use supervised learning."
)
add_paragraph(
    "Unsupervised learning has no labels. The model must find structure in data itself—grouping similar customers, discovering hidden patterns, or reducing "
    "dimensions. A recommendation system clusters users silently; anomaly detection finds rare outliers; dimensionality reduction finds the most important features. "
    "These problems are harder but unlock insights when you have no labels."
)
add_paragraph(
    "There's also reinforcement learning: the model acts in an environment, receives rewards or penalties, and learns to maximize reward. Video game AI, "
    "robotics, and trading bots use reinforcement learning. The agent learns by trial and error."
)

add_heading("2.2 The Bias-Variance Tradeoff: The Eternal Tension", level=2)
add_paragraph(
    "Every model faces a fundamental dilemma. Make it too simple (high bias), and it won't learn the true pattern—underfitting. A linear model on "
    "non-linear data. A decision tree with depth 1. Make it too complex (high variance), and it memorizes noise instead of patterns—overfitting. "
    "A decision tree that grows infinitely, fitting every single training example perfectly but failing on new data."
)
add_paragraph(
    "The sweet spot: find the model complexity where bias and variance balance. Complex enough to capture reality, simple enough to generalize. "
    "This is the bias-variance tradeoff, and it's one of the most important ideas in machine learning."
)

add_heading("2.3 Optimization: Descending the Loss Mountain", level=2)
add_paragraph(
    "Here's the magic engine: machine learning works by iteratively improving. You start with random weights. You compute how wrong you are (the loss). "
    "You ask: in which direction should I change the weights to reduce this loss? That direction is the gradient. You take a small step down—gradient descent. "
    "Repeat thousands of times, and your model improves."
)
add_code_block(
"""# The fundamental learning loop
for epoch in range(1000):
    # Forward: compute predictions
    predictions = model.predict(X_train)
    
    # Compute loss (how far off are we?)
    loss = mean_squared_error(predictions, y_train)
    
    # Backward: compute gradients (which direction to improve?)
    gradients = compute_gradients(loss, model.weights)
    
    # Update: take a small step toward improvement
    model.weights -= learning_rate * gradients
    
    # The loss decreases each iteration"""
)
add_paragraph(
    "In neural networks, backpropagation is the algorithm that computes these gradients efficiently by working backward through layers, using the "
    "chain rule from calculus. It's one of the most important algorithms ever discovered—without it, deep learning wouldn't be practical. With it, "
    "you can train networks with millions of parameters."
)

add_heading("2.4 The Zoo of Algorithms", level=2)
add_paragraph(
    "Your repository covers dozens of algorithms. The narrative: Linear regression fits a line to continuous data. Logistic regression adapts "
    "that for classification (spam/not spam). Decision trees grow branches based on questions—'Is age > 30?'—and recursively partition the data. "
    "Random forests combine thousands of trees, letting them be more robust than single trees."
)
add_paragraph(
    "Support vector machines find the optimal boundary between classes, with the widest margin. K-Nearest Neighbors classifies by finding similar "
    "training examples. Naive Bayes is probabilistic and surprisingly effective despite strong independence assumptions. Each algorithm has strengths "
    "and weaknesses; no single algorithm wins everywhere."
)
add_paragraph(
    "For unsupervised learning: K-Means clusters data into groups by minimizing within-cluster distance. PCA finds the principal components that "
    "explain the most variance, reducing dimensions. Autoencoders are neural networks that compress data and reconstruct it, learning compressed "
    "representations automatically."
)

add_separator()

# PART 3: DEEP LEARNING
add_heading("Part 3: The Deep Learning Revolution — Learning from Layers", level=1)

add_paragraph(
    "For decades, machine learning was limited. Classical algorithms hit scaling walls and feature engineering was tedious. Then came a revelation: "
    "you don't need hand-engineered features; you can let the model learn them. This is deep learning—neural networks with many layers, each learning "
    "progressively more abstract features. A raw image → edges → shapes → parts → objects. Very deep networks learn hierarchical representations."
)

add_heading("3.1 The Perceptron: The Founding Unit", level=2)
add_paragraph(
    "A perceptron is a simple binary classifier: take inputs, multiply each by a weight, sum them, apply a threshold—if above threshold, output 1; "
    "otherwise 0. It's a decision-maker for linearly separable data. A single perceptron can't solve non-linear problems (the famous XOR problem broke it)."
)
add_paragraph(
    "But here's the revolution: layer perceptrons together with non-linear activation functions (sigmoid, ReLU), and you can solve any problem. "
    "This is the multi-layer perceptron (MLP). Input layer receives raw features. Hidden layers gradually transform the data, each learning weights "
    "that capture increasingly complex patterns. Output layer makes the final prediction. The expressive power is enormous."
)

add_heading("3.2 Specialized Architectures for Specialized Problems", level=2)
add_paragraph(
    "MLPs are general, but specific problems need specialized structures. Convolutional Neural Networks (CNNs) are built for images. Instead of "
    "treating every pixel as independent, convolutions apply a sliding filter that recognizes local patterns—edges, textures, shapes. This "
    "drastically reduces parameters and captures the hierarchical structure of images. CNNs dominate computer vision."
)
add_paragraph(
    "Recurrent Neural Networks (RNNs) are built for sequences: text, audio, time series. They process tokens one by one, passing information "
    "forward so the network can 'remember' previous context. But RNNs struggle with long sequences—the gradient signal gets lost or explodes. "
    "This is the vanishing gradient problem."
)
add_paragraph(
    "LSTMs (Long Short-Term Memory) solve this with special gates: forget gate (what to discard), input gate (what to add), output gate (what "
    "to expose). These gates let the network maintain long-term dependencies. GRUs (Gated Recurrent Units) simplify LSTMs with fewer gates but "
    "similar power. These architectures enable language understanding and sequence generation."
)

add_heading("3.3 The Transformer: A Paradigm Shift", level=2)
add_paragraph(
    "In 2017, 'Attention is All You Need' changed everything. Transformers process entire sequences simultaneously (not step-by-step like RNNs). "
    "Each token attends to all other tokens, computing relevance scores. This parallelizes computation dramatically and captures long-range "
    "dependencies better than RNNs. 'The cat sat on the mat' — 'cat' can attend to 'sat' and 'mat' directly in one step, not sequentially."
)
add_code_block(
"""# Simplified transformer self-attention concept
# Each token learns to attend to every other token

tokens = ['The', 'cat', 'sat', 'on', 'mat']

# For 'cat', compute attention scores to each token
scores_for_cat = {
    'The': 0.1,   # low relevance
    'cat': 0.8,   # high relevance (itself)
    'sat': 0.7,   # moderately high (action)
    'on': 0.2,    # low
    'mat': 0.3    # low
}

# Weighted sum uses these scores
context_for_cat = weighted_sum(all_tokens, scores_for_cat)
# Result: 'cat' combines information from all tokens, weighted by relevance"""
)
add_paragraph(
    "Transformers are the foundation of all modern large language models. They're trained to predict the next token in a sequence—a simple task "
    "that teaches them language structure, factual knowledge, reasoning, and even creativity. ChatGPT, Claude, Gemini—all transformer-based."
)

add_paragraph(
    "The layers stack: self-attention lets tokens talk to each other; feed-forward networks transform each token; residual connections "
    "(skip connections) let gradients flow freely. The result: very deep networks that train efficiently. Transformers with 100+ layers are common."
)

add_heading("3.4 Generative Models: GANs, VAEs, and Diffusion", level=2)
add_paragraph(
    "Until now, we've discussed models that classify or predict. Generative models create new data. GANs (Generative Adversarial Networks) consist "
    "of two networks: a generator creates fake data; a discriminator judges if data is real or fake. They compete, driving the generator toward "
    "making increasingly realistic samples. GANs generate stunning images but are unstable to train."
)
add_paragraph(
    "VAEs (Variational Autoencoders) encode data into a latent (hidden) distribution and decode from it. They learn structured representations. "
    "Diffusion models generate samples by reversing a noise process: start with pure noise, gradually refine it toward a data point. Diffusion is "
    "now state-of-the-art for image generation (Stable Diffusion, DALL-E)—more stable than GANs, higher quality than VAEs."
)

add_separator()

# PART 4: GENAI
add_heading("Part 4: The GenAI Era — Language, Intelligence, and Emergence", level=1)

add_paragraph(
    "We reach the inflection point: massive transformers trained on the internet. Models that write, reason, code, converse. This is "
    "generative AI—and it's not just a bigger neural network. It's a qualitative leap. Emergent abilities appear: models reason about things "
    "never seen in training, follow complex instructions, and explain their reasoning. The story of why remains partly mysterious. But the "
    "mechanisms are fascinating."
)

add_heading("4.1 From Text to Meaning: Tokenization and Embeddings", level=2)
add_paragraph(
    "Language models work with numbers, not text. First step: break text into tokens (sub-words or words), then convert tokens into "
    "embeddings—vectors in a high-dimensional space. The magic: similar tokens (cat, kitten, feline) are close in vector space. Embeddings "
    "encode semantic meaning as geometry."
)
add_code_block(
"""# Text to embeddings pipeline
text = 'The cat sat on the mat'

# Step 1: Tokenize (hundreds of tokenization schemes exist)
tokens = tokenizer.encode(text)
# Example: [1, 5, 23, 18, 2, 15]

# Step 2: Embed (each token becomes a vector)
embeddings = model.embed(tokens)
# Each embedding is ~768 dimensional (in GPT-like models)

# Embeddings capture meaning: similar tokens are close
cos_sim(embed('cat'), embed('kitten')) = 0.92  # Very similar
cos_sim(embed('cat'), embed('car')) = 0.45     # Somewhat similar"""
)
add_paragraph(
    "Word2Vec pioneered this idea: train a shallow network to predict context words from a target word; the hidden layer is your embedding. "
    "Modern transformers learn contextualized embeddings: 'cat' in 'The cat sat' has a different embedding than 'cat' in 'Let's discuss the cat food industry.' "
    "Contextualization is crucial for language understanding."
)

add_heading("4.2 The LLM Training Pipeline: Three Stages to Intelligence", level=2)
add_paragraph(
    "Training a large language model is a three-stage process, each adding capabilities:"
)
add_paragraph(
    "Stage 1 (Pretraining): Feed massive unlabeled internet text (books, websites, code, conversations). Objective: predict the next token. "
    "The model learns language structure, facts, reasoning. This takes thousands of GPUs and months. Models learn to write coherent text, "
    "answer factual questions, and generate code. But they're not yet aligned with human values."
)
add_paragraph(
    "Stage 2 (Supervised Fine-tuning): Show the model examples of good responses to prompts. Curate high-quality (prompt, response) pairs. "
    "Train the model to mimic these good responses. The model learns instruction-following and becomes more chatbot-like. This stage is cheaper "
    "and faster than pretraining."
)
add_paragraph(
    "Stage 3 (Reinforcement Learning from Human Feedback): Have humans rank multiple model responses to the same prompt. Train a reward model "
    "that learns to score responses like humans do. Use reinforcement learning (specifically, Proximal Policy Optimization) to make the LLM "
    "maximize this reward. The result: models that are helpful, harmless, and honest. This is how ChatGPT becomes ChatGPT, not just a text predictor."
)
add_code_block(
"""# Simplified LLM training pipeline

# Stage 1: Pretraining (unsupervised)
for batch in massive_internet_corpus:
    predicted_next = model.predict_next_token(batch)
    loss = cross_entropy(predicted_next, actual_next)
    backprop(loss)
    # After months: model learns language

# Stage 2: Supervised fine-tuning
for (prompt, good_response) in curated_examples:
    model_response = model.generate(prompt)
    loss = cross_entropy(model_response, good_response)
    backprop(loss)
    # Now model follows instructions

# Stage 3: RLHF
for prompt in diverse_prompts:
    responses = [model.generate(prompt) for _ in range(4)]
    human_ranks = [rank_response(r) for r in responses]
    reward_predictions = reward_model.score(responses)
    
    # RL: maximize reward for top-ranked responses
    policy_loss = rl_loss(model, reward_predictions)
    backprop(policy_loss)
    # Result: aligned, helpful model"""
)

add_heading("4.3 Fine-tuning for Specialization", level=2)
add_paragraph(
    "Pretraining a 7B parameter model costs millions. But you can adapt pretrained models to your task cheaply. Fine-tuning updates all weights "
    "on your data. LoRA (Low-Rank Adaptation) and QLoRA (Quantized LoRA) update only low-rank modifications—you freeze most weights and learn only "
    "small adapters. This makes fine-tuning possible on consumer GPUs."
)
add_paragraph(
    "The result: specialized models. Fine-tune on medical papers and get a medical Q&A system. Fine-tune on legal documents and get a legal assistant. "
    "Fine-tune on customer support chats and get a customer service bot. Transfer learning—using knowledge from pretraining for new tasks—is one of "
    "the biggest wins in modern AI."
)

add_separator()

# PART 5: RETRIEVAL AND AGENTS
add_heading("Part 5: Grounding AI in Reality — RAG, LangChain, and Agents", level=1)

add_paragraph(
    "LLMs are powerful reasoners, but they have constraints: they only know what's in training data. If your proprietary document weren't "
    "online, the model won't know it. But businesses need AI to answer questions about their internal knowledge. Enter retrieval-augmented "
    "generation (RAG): the LLM retrieves relevant documents first, then generates answers based on them."
)

add_heading("5.1 Vector Databases and Semantic Search", level=2)
add_paragraph(
    "The key innovation: embed your documents (convert to vectors), store in a database, and search by meaning not keywords. When a user asks "
    "a question, embed it, search for similar document embeddings, and pass those documents as context to the LLM."
)
add_code_block(
"""# RAG workflow

# Setup: Embed and store documents once
documents = load_company_documents()  # PDFs, docs, webpages
embeddings = model.embed(documents)
vector_db.store(embeddings, documents, metadata)

# At inference time: retrieve context then generate
user_query = 'What was Q3 revenue?'
query_embedding = model.embed(user_query)
similar_docs = vector_db.search(query_embedding, top_k=5)
# Returns the 5 most similar documents

# Generate with context
context = '\\n'.join(similar_docs)
prompt = f'Context: {context}\\n\\nQuestion: {user_query}\\n\\nAnswer:'
answer = llm.generate(prompt)"""
)
add_paragraph(
    "Vector databases (ChromaDB, Pinecone, FAISS, Weaviate) make this practical. This unlocks RAG applications: document search, customer support bots "
    "with company knowledge, research assistants, internal Q&A systems. RAG dramatically improves LLM reliability by grounding answers in real data."
)

add_heading("5.2 LangChain: Framework for LLM Applications", level=2)
add_paragraph(
    "Building complex LLM applications needs structure. Prompt templates separate logic from data. Chains connect multiple steps. Memory persists context "
    "across turns. Agents decide which tools to use. LangChain provides all this."
)
add_code_block(
"""from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_core.llms import OpenAI

# Prompt template: reusable structure
template = '''You are an expert analyst.
Document: {doc}
Question: {question}
Provide a concise answer.'''

prompt = PromptTemplate(
    template=template,
    input_variables=['doc', 'question']
)

# Chain: connect LLM with prompt
chain = LLMChain(llm=OpenAI(), prompt=prompt)

# Use: clean, reusable
result = chain.run(
    doc=retrieved_document,
    question=user_question
)"""
)
add_paragraph(
    "Prompt templates keep logic clean. Chains make workflows testable and modular. Building LLM applications becomes like traditional software "
    "engineering: composable, reusable, maintainable. LangChain is one of the most important tools in modern AI development."
)

add_heading("5.3 Agents: LLMs as Decision-Makers", level=2)
add_paragraph(
    "LLMs are powerful reasoners, but they can't take actions. They can't call your database, send emails, or do calculations directly. But they "
    "can decide which tools to use. An agent is an LLM equipped with tools and the reasoning to select them."
)
add_paragraph(
    "An agent receives a user request, reasons about what information or actions are needed, calls appropriate tools, interprets results, and "
    "generates a final answer. Example: 'Send me a report of Q3 revenue by region.' The agent reasons: 'I need to query the database, format the results, "
    "and return them.' It calls tools sequentially."
)
add_code_block(
"""# Agent with tools
from langchain.agents import Tool, initialize_agent

tools = [
    Tool(
        name='query_database',
        func=query_company_db,
        description='Query company financial database'
    ),
    Tool(
        name='send_email',
        func=send_email,
        description='Send an email to a recipient'
    ),
    Tool(
        name='format_report',
        func=format_as_table,
        description='Format data as a nicely formatted table'
    )
]

agent = initialize_agent(
    tools,
    llm,
    agent='zero-shot-react-description'
)

# Agent decides to use which tools and in what order
result = agent.run('Send me Q3 revenue by region as a table')"""
)
add_paragraph(
    "Agents enable chatbots, research systems, and autonomous workflows. They're the bridge between LLM reasoning and real-world action."
)

add_separator()

# PART 6: ORCHESTRATION
add_heading("Part 6: Scaling Intelligence — Multi-Agent Orchestration", level=1)

add_paragraph(
    "One agent is powerful. Multiple agents working together are transformative. Specialized agents excel at their roles. One researches, "
    "another summarizes, a third fact-checks. A coordinator routes tasks. This is multi-agent orchestration."
)

add_heading("6.1 Orchestration Patterns", level=2)
add_paragraph(
    "Sequential orchestration: Agent A completes, then Agent B begins. Agent A researches a topic; Agent B summarizes findings. "
    "This pattern is reliable and easy to understand but slower (must wait for Agent A to finish)."
)
add_paragraph(
    "Parallel orchestration: Multiple agents work simultaneously, results merged. Agent A searches web; Agent B queries your database; "
    "Agent C checks facts. Results combine. Faster but harder to coordinate."
)
add_paragraph(
    "Hierarchical orchestration: A manager agent assigns tasks to worker agents. Manager reasons what's needed, dispatches to specialists, "
    "collects results, generates final response. Elegant for complex problems."
)

add_heading("6.2 Building Production GenAI Systems", level=2)
add_paragraph(
    "The production stack: API layer (user interface), orchestration layer (LangChain/LangGraph for workflows), "
    "model layer (LLMs from OpenAI/open-source), retrieval layer (vector DB for context), tool layer (integrations to databases/APIs), "
    "and feedback loop (human reviews to improve alignment)."
)
add_paragraph(
    "Advanced topics emerging: Chain-of-thought prompting (ask model to think step-by-step for better reasoning). Multimodal models (text + images). "
    "Vision transformers (attention for images). Prompt engineering (crafting instructions to unlock capabilities). Mixture-of-experts (routing tokens "
    "to specialized sub-models for efficiency). These frontiers are active research."
)

add_separator()

# CONCLUSION
add_heading("Conclusion: The Unified Picture", level=1)

add_paragraph(
    "You've now journeyed from matrix multiplication to multi-agent systems. The story is coherent:"
)

add_paragraph(
    "It starts with mathematics—linear algebra as the language, probability for reasoning under uncertainty, statistics for learning from samples. "
    "These provide the foundation."
)

add_paragraph(
    "Machine learning algorithms climb that foundation, discovering that optimization by gradient descent can find patterns in data automatically. "
    "Supervised learning tags data with labels; unsupervised finds hidden structure. Classical algorithms work but hit scaling walls."
)

add_paragraph(
    "Deep learning shatters those walls. Layered transformations learn hierarchical representations. Convolutional layers sense images; recurrent layers "
    "remember sequences; transformers attend globally. Very deep networks surprise us with emergent reasoning."
)

add_paragraph(
    "Large language models amplify this: train transformers on enough data with enough parameters, and language understanding emerges. But raw capability "
    "isn't enough for production. Retrieval-augmented generation grounds models in real knowledge. LangChain organizes complex workflows. Agents enable "
    "real-world action. Multi-agent orchestration solves complex problems."
)

add_paragraph(
    bold=True,
    text="Each layer builds on those below. Understand this connection, and you understand modern AI. "
)

add_paragraph(
    "Next time you use ChatGPT, see Stable Diffusion generate an image, or watch a recommendation system predict your preferences—recognize the "
    "components: the math, the optimization, the transformed information flowing through layers, the retrieved context, the orchestrated agents. "
    "You now know how it works. More importantly, you can build it."
)

add_separator()

add_heading("Repository Quick Reference", level=1)
add_paragraph("Basics/: Vectors, matrices, eigenvalues, covariance, correlation, probability, statistics, hypothesis testing, bias-variance, dimensionality reduction")
add_paragraph("ML/: Linear regression, logistic regression, decision trees, random forests, SVMs, KNN, naive bayes, K-Means, PCA, autoencoder, ensemble methods, feature engineering")
add_paragraph("DL/: Perceptron, MLP, CNN, RNN, LSTM, GRU, transformer, seq2seq, GAN, VAE, diffusion, activation functions, loss functions, backpropagation, training techniques")
add_paragraph("GenAI/: LLMs, tokenization, embeddings, Word2Vec, transformers, self-attention, GPT/BERT, pretraining, fine-tuning, LoRA, QLoRA, RLHF, RAG, LangChain, ChromaDB, agents, orchestration")
add_paragraph("Python/: Data structures, NumPy, Pandas, NumPy, generators, decorators, context managers, serialization, ML patterns")

add_separator()
add_paragraph(
    "This narrative connects 140+ repository topics into one coherent story. Dive into individual files knowing their place in the larger whole.",
    italic=True
)

doc.save(output_path)
print(f'✓ Generated {output_path}')
print(f'✓ Comprehensive narrative covering all topics from math foundations to multi-agent systems.')
