#  ╓─────[ libft ]─[ v0.0.1 ]  
#  ║ Created by: undefined (undefined)
#  ║ Created at: Tue Nov  7 14:40:48 CET 2017
#  ║ Last Edited: Tue Nov  7 14:40:48 CET 2017
#  ╙─────────────────────────────────────────── ─ ─ 

#  ╓─────[ Target ]─  
#  ╙───────────────────── ─ ─ 
NAME = libft.a

#  ╓─────[ Compiler ]─  
#  ╙───────────────────── ─ ─ 
CC = gcc
CCFLAGS = -Wall -Werror -Wextra -ansi -pedantic

#  ╓─────[ Directories ]─  
#  ╙───────────────────── ─ ─ 
INCLDIRS = ./

#  ╓─────[ Functions ]─  
#  ╙───────────────────── ─ ─
S_CORE =
S_IO =
S_STRING =
S_PREDICATE =
S_DS =
S_MATH =
S_FP =

FUN = $(S_CORE) $(S_IO) $(S_STRING) $(S_PREDICATE) $(S_DS) $(S_MATH) $(S_FP)  
O_FUN = $(FUN:.c=.o)

all: $(NAME)

$(NAME): $(O_FUN)
	@ar rcs $(NAME) $(O_FUN)
	@echo "\n\033[0;32m [OK] \033[0m \033[0;33m Linking library:\033[0m " $(NAME)

%.o : %.c 
	@echo "\033[0;32m [OK] \033[0m \033[0;33m Compiling:\033[0m " $@
	@$(CC) $(CCFLAGS) -I$(INCLDIRS) -c -o $@ $<

clean:
	@/bin/rm -Rf $(O_FUN)

fclean: clean
	@rm -f $(NAME)
	@echo  "\033[0;31m [✗] \033[0m \033[0;33m Removed last build: \033[0m " $(NAME)

re:
	@$(MAKE) fclean
	@$(MAKE) all

#  ╓─────[ Call me maybe ]─  
#  ╙───────────────────── ─ ─ 
.PHONY: all clean fclean re
