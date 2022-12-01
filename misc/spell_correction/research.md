# Spell correction model


## Research:

### Traditional approach
  
Peter-Norvig:  This algorithm based spell check and correction using edit-distance based method.

[How to Write a Spelling Corrector](https://norvig.com/spell-correct.html)

[Spelling Correction: How to make an accurate and fast corrector](https://towardsdatascience.com/spelling-correction-how-to-make-an-accurate-and-fast-corrector-dc6d0bcbba5f)

  
Symspell:

[Fast Word Segmentation of Noisy Text](https://towardsdatascience.com/fast-word-segmentation-for-noisy-text-2c2c41f9e8da)

### Advantages
- Quicker in spell correction compared to DL based approach.
- Less complex methods and easy to create.


  
### DL approach

Seq-to-Seq problem: Sentence with typos and spelling issues as input and output is spell corrected sentences with context understanding.

DeepCorrector:  
[DeepCorrection 3: Spell correction and simple grammar correction](https://praneethbedapudi.medium.com/deepcorrection-3-spell-correction-and-simple-grammar-correction-d033a52bc11d)


Neural Spell correction:  
[https://github.com/neuspell/neuspell](https://github.com/neuspell/neuspell)


### Advantages
- Helps in good candidate selection based on contextual understanding.
- Not just mispelled words, grammatical mistakes can also be rectified.