""" ex_file_path = C:/User/Your_Name/Desktop/Class/ClassFiles"""
file_path = YOUR_WORKING_DIRECTORY
""" Will ignore footer and header tags  
ex: IGNORE_TAGS = ('footer', 'header')
When a footer or header is found, it will ignore their current line"""
IGNORE_TAGS = ( YOUR_TAGS_HERE )
""" Unlike ignore, will skip over ENTIRE tag and it's contents
 ex: SKIP_TAGS = ('nav', 'h1')
 When a nav or h1 is found, it skip over all text and leave it untouched"""
SKIP_TAGS = ( YOUR_TAGS_HERE )
CUSTOM_EDIT = (YOUR_TAG_HERE)
LOREM_IPSUM = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et " \
              "dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut " \
              "aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum " \
              "dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui " \
              "officia deserunt mollit anim id est laborum. Sed ut perspiciatis unde omnis iste natus error sit " \
              "voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore " \
              "veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia " \
              "voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione " \
              "voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, " \
              "consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore " \
              "magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam " \
              "corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure " \
              "reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem " \
              "eum fugiat quo voluptas nulla pariatur? "

CUSTOM_EDIT_TEXT = TEXT_TO_REPLACE_IN_TAG