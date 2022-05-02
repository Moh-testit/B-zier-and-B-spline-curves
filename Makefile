##
## EPITECH PROJECT, 2021
## B-MAT-500-COT-5-1-309pollution-mohamed.mazu.git-mohamed.mazu
## File description:
## Makefile
##

NAME	=	309pollution

all:	$(NAME)

$(NAME):
		ln -s 309pollution.py $(NAME)
		chmod +x $(NAME)

clean:
		rm -rf *~
		rm -rf __pycache__

fclean:	clean
		rm -rf $(NAME)

re:	fclean all
