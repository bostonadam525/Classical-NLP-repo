# Word Sense, Abbreviation and Acronym Disambiguation

## Overview
* In natural language processing (NLP), word sense disambiguation (WSD) is the task of determining the correct sense of a word based on the surrounding context. WSD is considered a classification problem, in which given an ambiguous word and every possible meaning, the goal is to classify it into one of its sense’s classes based on the context.
* Disambiguating abbreviations is considered as a sub-type/sub-task of word sense disambiguation (WSD).
* This repository contains resources for general WSD tasks as well as Abbreviation and Acronym WSD.

## HuggingFace/Github Repos

1. SpanMarker with bert-base-cased on Acronym Identification
   * This is a SpanMarker model trained on the Acronym Identification dataset that can be used for Named Entity Recognition. This SpanMarker model uses bert-base-cased as the underlying encoder.
   * HuggingFace Repo: https://huggingface.co/tomaarsen/span-marker-bert-base-acronyms
  

2. SpanMarker with bert-base-uncased on Acronym Identification
   * This is a SpanMarker model trained on the Acronym Identification dataset that can be used for Named Entity Recognition. This SpanMarker model uses bert-base-uncased as the underlying encoder.
   * HuggingFace Repo: https://huggingface.co/tomaarsen/span-marker-bert-base-uncased-acronyms
  
3. DistilBERT Fine-tuned on MeDAL Dataset for Medical Abbreviation Disambiguation
   * This repository hosts a DistilBERT model that has been fine-tuned on the MeDAL dataset, a comprehensive dataset designed for the disambiguation of medical abbreviations to enhance natural language understanding (NLU) in the medical domain. This model aims to provide an efficient and reliable solution for understanding and interpreting medical texts, which are often laden with abbreviations and acronyms that can have multiple meanings based on their context.
   * HuggingFace Repo: https://huggingface.co/jamesliounis/MeDistilBERT
  
4. GLADIS
   * GLADIS: A General and Large Acronym Disambiguation Benchmark (Long paper at EACL 23) under the CC0-1.0 license.
   * In this paper, the authors proppose a new Benchmark named Gladis and an acronym linking system named AcroBERT.
   * AcroBERT can do end-to-end acronym linking. Given a sentence, our framework first recognize acronyms by using MadDog (CC BY-NC-SA 4.0), and then disambiguate them by using AcroBERT.
   * Github: https://github.com/tigerchen52/GLADIS
   * HuggingFace repo: https://huggingface.co/spaces/Lihuchen/AcroBERT
  
5. Analysis of BERT for Word Sense Disambiguation
   * arxiv paper: Analysis and Evaluation of Language Models for Word Sense Disambiguation. link: https://arxiv.org/abs/2008.11608
   * github: https://github.com/danlou/bert-disambiguation/tree/master


## WSD Papers

* Charbonnier et al. 2018. Using Word Embeddings for Unsupervised Acronym Disambiguation. Proceedings of the 27th International Conference on Computational Linguistics, pages 2610–2619. link: https://aclanthology.org/C18-1221.pdf
  
* jaber at al. 2022. Disambiguating Clinical Abbreviations Using a One-Fits-All Classifier Based on Deep Learning Techniques. Methods of Information in Medicine Vol. 61 No. S1/2022. link: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9246508/pdf/10-1055-s-0042-1742388.pdf
  
* Li et al. 2015. Acronym Disambiguation Using Word Embedding. Proceedings of the Twenty-Ninth AAAI Conference on Artificial Intelligence. link: https://cdn.aaai.org/ojs/9713/9713-13-13241-1-2-20201228.pdf
  
* Song et al. 2022. T5 Encoder Based Acronym Disambiguation with Weak Supervision. Scientific Document Understanding Workshop at AAAI 2022, March 1. link: https://ceur-ws.org/Vol-3164/paper18.pdf

* Wu et al. 2022. Prompt-based Model for Acronym Disambiguation via Negative Sampling. AAAI’22: Scientific Document Understanding. link: https://ceur-ws.org/Vol-3164/paper26.pdf

* Zhong et al. 2022. Leveraging Domain Agnostic and Specific Knowledge for Acronym Disambiguation. arXiv:2107.00316v1 [cs.AI] 1 Jul 2021. link: https://arxiv.org/pdf/2107.00316


  

