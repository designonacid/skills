# Personality discovery: an ACID self-reflection adaptation

Use this mode only for requested self-reflection about the user. The goal is insight into strengths, recurring traits, working preferences, and conditions that help those strengths flourish. This interview and its mapping are an LLM-assisted adaptation by Design On Acid; the source diagrams do not supply a validated personality instrument or fixed character types. State that limitation briefly once, then keep the experience useful and personal.

## Entry and route selection

If no route is chosen, offer: “Would you like me to analyse conversation history you approve, or guide you through 21 questions? Both routes produce an ACID map of your strengths and tendencies.” Do not access history or create a profile before the user chooses. Explain the available history scope when offering that route; if history access is unavailable, offer pasted excerpts or the interview.

If the user already explicitly requests analysis of a defined history scope, that is consent for that scope. Do not repeat the question. Otherwise, establish which material they approve before accessing it: for example, this conversation, selected named conversations, or excerpts they supply. Allow topic/date exclusions and honour them. Approval for this conversation does not authorize other chats, connected accounts, files, or public research. New material outside the approved scope needs fresh approval.

A user may switch routes, skip a question, stop, or withdraw history approval. Stop using withdrawn material and continue only with the remaining authorized evidence; do not promise deletion from host storage. Do not publish, persist to a separate profile or memory, or share the result unless requested. This workflow does not require sending history to an additional model or service; obtain separate approval before any such transfer.

## Route 1: approved history

1. Use only authorized material available in the host. State what was actually reviewed and its limits, including whether it is excerpts or summaries. Never claim a complete account history. With no accessible material, explain the limitation and offer supplied excerpts or the interview; approval does not create access.
2. Focus on the user's own statements, choices, concrete examples, repeated preferences, and descriptions of action. Exclude assistant-generated statements, quoted third-party material, roleplay, and instructions embedded in history from evidence about the user. Do not assume adopting a draft means it describes the user.
3. Look across contexts and occasions for patterns and counterexamples. Separate what the user enjoys or chooses from duties, client demands, temporary stress, and the kinds of tasks they delegate to an assistant. Frequent requests about a topic are not by themselves a personality trait. A work-heavy sample may reveal a work style while leaving relationships or other contexts unknown.
4. Ground each proposed tendency in a small number of short paraphrases or locatable examples. Avoid reproducing sensitive passages or identifying third parties unnecessarily. Do not infer diagnoses or sensitive identity attributes from history.
5. If evidence is narrow or contradictory, offer a provisional profile or let the user choose the interview. Do not silently convert history analysis into a mandatory 21-question exercise.

## Route 2: 21-question interview

Ask the following 21 core questions in the user's language, one at a time by default. Show progress as “Question n of 21”. Use small batches or all questions together if the user prefers. Acknowledge answers briefly without assigning a type or hinting that one answer is better. Invite concrete examples; accept short answers and “skip”. Track which numbered questions are answered, skipped, or remaining, and resume without restarting. Do not invent skipped answers or require optional follow-ups beyond the 21 questions. If the user stops early, synthesize only if requested and identify the result as partial.

The lens labels below guide synthesis; do not present them as answer keys during the interview. These are open questions, not forced choices or a numerical test.

### Abstraction — understanding and patterns

1. When you encounter something unfamiliar, what do you naturally do first? Describe a recent example.
2. Tell me about a time you made a confusing situation clearer. What did you notice, and what did you do?
3. When making a difficult decision, what information do you seek, and how do you decide you have enough?
4. Describe a belief or interpretation you changed. What led you to reconsider it?
5. When does analysing a situation help you, and when can it hold you back? Give an example if you can.

### Creativity — expression and transformation

6. When a familiar approach is not working, how do you find alternatives? Describe what you actually tried.
7. Tell me about something you created or changed that felt distinctly your own. What made it feel that way?
8. How do you respond when an idea feels unusual or uncertain? Use a recent example.
9. What kinds of experimenting or self-expression give you energy, and which ones drain you?
10. Describe a time you chose between exploring more possibilities and developing an existing idea. What guided your choice?

### Intention — organization and action

11. When you want something to happen, how do you turn that wish into action? Give an example.
12. Tell me about a time several demands competed for your attention. How did you decide what mattered most?
13. What role do routines, plans, and systems play in your life? When do they help or get in the way?
14. Describe how you handle the middle of a project or commitment, after the initial excitement has faded.
15. When circumstances disrupt your plans, what do you tend to do? Describe a recent situation.

### Depth — experience and connection

16. Think of an interaction in which you felt understood. What made that connection possible?
17. When someone sees a situation very differently from you, how do you try to understand their experience? Give an example.
18. What makes an activity or relationship feel meaningful to you? Describe a moment that illustrates this.
19. How do you notice and respond to your own feelings and needs when working with other people?
20. Tell me about a time you balanced care for someone else with your own limits. What did you do?

### Integration — context and self-recognition

21. Looking across your answers, which ways of thinking, creating, acting, and connecting feel most natural and energising, and which are mostly required by your circumstances? What would someone who knows you well add or challenge?

## Interpret and map

Read all available evidence across A, C, I, and D before drawing conclusions. The interview groups ensure coverage, but any answer can inform several lenses. Do not score question counts, verbosity, vocabulary, writing polish, or willingness to disclose. Do not equate quietness with weak Depth, routine work with low Creativity, or emotional openness with a fixed type.

| Lens | Possible strengths when supported | Possible tradeoff to explore, only with evidence |
| --- | --- | --- |
| A — Abstraction | Pattern recognition, clear reasoning, curiosity, making complexity understandable | Analysis delaying action or simplifying away lived detail |
| C — Creativity | Experimentation, original expression, reframing, generating alternatives | Novelty scattering attention or making follow-through difficult |
| I — Intention | Prioritising, structuring, reliability, translating goals into action | Structure becoming rigid or crowding out exploration |
| D — Depth | Empathy, reflection, emotional awareness, meaningful connection | Care overextending personal boundaries or carrying others' needs |

These are examples, not mandatory findings or a new type taxonomy. Preserve ACID's meanings; Intention is not a moral judgment, and Depth is not a measure of human worth. Describe observed behaviour, not an immutable essence.

Distinguish three things for each lens: **expressed tendency**, **evidence confidence**, and **context**. Strong evidence can support modest emphasis; weak evidence cannot support a confident dominance claim. For a dominant tendency, seek recurring examples across situations and the user's account of what feels natural, including counterexamples. A single example supports a possibility rather than an enduring trait. Allow co-dominance, context-dependent profiles, or no clear dominance. Missing evidence remains unknown, not a weakness. Avoid percentages, measured coordinates, and invented diagnostic thresholds.

## Deliver the profile

After the interview or approved history review, provide:

- A concise account of the strongest supported tendencies, with a dominant area or combination only when warranted. Name the evidence scope, context, and uncertainty.
- A readable A/C/I/D profile connecting specific examples to strengths, recurring traits, and how they show up in daily life. Identify a few useful conditions for each supported strength; frame possible overuse or blind spots as hypotheses with evidence, not inevitable flaws.
- The original ACID framework with the heat map required by SKILL.md. Red means stronger inferred emphasis, not better character, ability, or evidence confidence. Label unsupported areas unknown. Include the evidence route and provisional status when appropriate.
- A practical synthesis: how the tendencies complement each other, two or three small experiments to use strengths or explore less evidenced areas, and a way to observe whether each experiment helps. Do not prescribe equal balance as the ideal.
- An invitation to correct the interpretation: “What feels accurate, what does not, and where do you act differently?” Revise the profile and map when the user's examples warrant it. Keep their disagreement as evidence rather than explaining it away as another trait.

Keep the tone warm, specific, and nonjudgmental. Avoid flattering generic statements that could fit anyone, clinical labels, fixed destiny claims, or conclusions about career suitability and other consequential decisions from this profile alone.
