<!-- This is a comment block in Markdown. When the document is rendered, you won't see this text.

If you need help on MarkDown syntax, you can look at the guide here: https://www.markdownguide.org/basic-syntax/.
You are also welcome to ask the Module instructors for help with writing MarkDown.

You can use this template as the starting point for your report.
Answer the questions by writing your answers in the space between the bullet points.
If you are editing this file in VSCode, you can press CTRL+K then V to open a preview of the document.

Comment blocks end by closing the "arrow" we opened at the start. -->

# Determining Depot Locations: Report

<!-- This module is anonymously marked - please DO NOT include your name! -->
Candidate Number: 24223495

<!-- The headers that follow correspond to all questions in the assignment that require a written answer. 

You can write as much as you like for your answers in the space provided.
However please bear in mind that a good answer and a long answer are not necessarily the same thing! -->

## `Location` equality

1. Why might the definition of "equal" not be desirable, if we did not have the assurance from CLtd at the start of this task?

In the event that two Locations with name "X" are in the same region, then the equality operator would return True when comparing these two locations, despite them being seperate locations and the correct return value being False.

2. Are there any problems you foresee with this definition of "equal", even with the assurance (at the start of this task) from CLtd?

If there was a depot with name "X" in region "R" but also a settlement in region "R" at a DIFFERENT location with name "X", then this defenition of "equal" would return that these are the same location, despite the correct return value being false.

3. Suggest an idea for avoiding / resolving the problem you raised in point 2, if you identified any. Choose one of your choice if you identified multiple issues. **Do not** implement this idea in your code, however.

The defenition of "equal" should include a comparison of the 'depot' attribute for the two locations being tested and only return true if the 'depot' attributes are identical.

## Fastest Trip From a Given `Location`

1. Is it possible, even after the tie-breakers given in the assignment task, for there to still be multiple entries in `potential_locations` to choose as the closest? (Yes/ No)

No

2. If not, why not? If so, what are the circumstances under which this could happen?

Given the assurances given by CLtd, it is not possible that there exists multiple settlement locations with identical name and region attributes in the same Country object.

3. How can you edit the method to fix the problem (if there is one) without forcing an error to be thrown? (Do not forget, you should implement these fixes in your code if you identify any here).

## Execution Time for the NNA

1. Identify (at least) one aspect of the `regular_n_gon` that makes it difficult to understand, or that might make it difficult to understand in the future. Suggest how this might be addressed.

A lack of in-line comments in the creation of the settlements makes the purpose of this code difficult to infer without further context. To ammend this, add in-line comments specifically explaining the mathematics behind the creation of the polar angles and the functions and methods used to create the settlment names.

2. Assess the advantages and disadvantages of using `Country`s like those generated from `regular_n_gon` for gathering the execution times $t_{\text{exe}}$, as opposed to a `Country` like the one in `locations.csv` or a `Country` with randomly-distributed settlements. You should give at least one advantage or one disadvantage.

An advantage would be the reduced complexity of the structure of settlements given by the regular_n_gon function compared to a random structure. The reduced complexity leads to simpler calculations for the travel time between settlements, which for large number of locations will lead to a noticably more efficient execution time.

A disadvantage would be that structures produced by the regular_n_gon function are idealised and not very realistic test data. This could lead to discrepancies in the scaling of execution time compared to more random, real structures with large numbers of settlements.

3. Comment on the relationship between the execution time $t_{\text{exe}}$ and number of settlements $N_{\text{locs}}$, given the data in your plot. You should include your plot as an image here.

My excecution times were unable to be computed in a reasonable time by my computer. The relationship between excecution time and number of settlements that I would expect from a plot, if one was produced, would be that the execution time (t) is proportional to the number of settlements (N) factorial. t = O(N!).

![This line will include your plot as an image in your report. This text will be displayed if your plot file cannot be found.](./nna_execution_times.png)

4. Why do you think $t_{\text{exe}}$ and $N_{\text{locs}}$ have this kind of relationship?

I think that the execution time will have this type of dependancy on the number of settlements because in the nearest neighbor algorithm, the travel time between each pair of settlements must be computed. For N settlements this leads to N! calls of the travel_time function and it is this that is the primary contribution to the execution time.
