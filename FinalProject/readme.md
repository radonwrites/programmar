Original plan: Create an AR app that would overlay words on a blank piece of paper, serving as the little push we writers need to actually start marking up a blank page sometime. Ideally the words can come from a bank of user generated inputs, and even more ideally the final result can be captured though an in-app camera button, or something like Google Lens can read the data and put it in a document.

The overall objective here was to create an interactive writing prompt system and tackle the daunting blank page (though the writer still has to be the one to make a permanent mark upon it)

Actual product: Random words (from an array) appear on paper when you place a tarot card in the top left corner. The "Le Monde" card generates a writing prompt you can start with. You can screenshot the image with your phone's screenshot capabilities. 

This is in some steps a little closer to a bigger picture goal, and helps substantiate the idea of incorporating physical artifacts into something that could be strictly digital.

** The code I wrote is in all "RTGen" files, and "TextAppear" (not used in the app currently). I used references and resources online to find the right terms to use. "CameraFocus" is something I found online, source in the comments. Without it, the camera doesn't autofocus which was an issue.

I could write a novel (no prompts needed) about all the problems I ran into. What's frustrating is, had I done everything correctly from the start, what took hours/days would have maybe, maaaaybe taken only an hour. Or less. Though I suppose this is the nature of learning to code.

The biggest challenges I faced were:
- My own lack of knowledge about C# and Unity: basically an overarching influence over all of these other problems...
- ARFoundations + Android: I wanted to use ARFoundations, becuase it is built into Unity, will not incur a monthly fee, and overall seems like the better long term solution
- TextMesh + writing text inputs through code
- making text random
- getting ideas but not getting too sidetracked by them

Next steps
- maybe make cards more random and have multiple cards read at once
- make words from cards "transferrable" or collectable, to be placed elsewhere
- add user input option
- use Model Target and assign word arrays to physical objects

Ultimately, I would like to make an app where the end user can walk around and "collect" associations and memories other users attribute to physical objects, and then assemble them (manually or randomly) into a prompt or start of a story.

Not yet sure on the final output - whether it's a system where something physically holds your phone up and you can write while looking through the screen, an image of paper with words overlayed, a "bank" of data you can reference (on your phone but not with the AR camera, so you can set it down and reference), or somehow uploadable to a digital document