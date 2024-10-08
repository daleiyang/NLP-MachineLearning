/*
 * lex functions test program.
 * 
 * @author    chenxin
 * @see        http://www.webssky.com 
 */
#include "friso.h"

#include <stdio.h>
#include <time.h>
#include <string.h>

#define __LENGTH__ 15
#define ___PRINT_HELP_INFO___                                    \
    printf("1. help print the current menu.\n");                \
printf("2. #set set the classify of the dictionary.\n");    \
printf("3. other search the words in the dictionary.\n");    \
printf("4. quit exit the programe.\n");

int main(int argc, char **argv)
{
    lex_entry_t e;
    int lex = __LEX_CJK_WORDS__;
    char _line[__LENGTH__];
    clock_t s_time, e_time;
    friso_t friso;

    s_time = clock();

    friso = friso_new();
    friso->dic = friso_dic_new();
    friso_config_t config = friso_new_config();
    //__CJK_WORDS__
    friso_dic_load( friso, config, __LEX_CJK_WORDS__, "../vendors/dict/UTF-8/lex-main.lex", __LENGTH__ );
    friso_dic_load( friso, config, __LEX_CJK_WORDS__, "../vendors/dict/UTF-8/lex-admin.lex", __LENGTH__ );
    friso_dic_load( friso, config, __LEX_CJK_WORDS__, "../vendors/dict/UTF-8/lex-chars.lex", __LENGTH__ );
    friso_dic_load( friso, config, __LEX_CJK_WORDS__, "../vendors/dict/UTF-8/lex-cn-mz.lex", __LENGTH__ );
    friso_dic_load( friso, config, __LEX_CJK_WORDS__, "../vendors/dict/UTF-8/lex-cn-place.lex", __LENGTH__ );
    friso_dic_load( friso, config, __LEX_CJK_WORDS__, "../vendors/dict/UTF-8/lex-company.lex", __LENGTH__ );
    friso_dic_load( friso, config, __LEX_CJK_WORDS__, "../vendors/dict/UTF-8/lex-festival.lex", __LENGTH__ );
    friso_dic_load( friso, config, __LEX_CJK_WORDS__, "../vendors/dict/UTF-8/lex-flname.lex", __LENGTH__ );
    friso_dic_load( friso, config, __LEX_CJK_WORDS__, "../vendors/dict/UTF-8/lex-food.lex", __LENGTH__ );
    friso_dic_load( friso, config, __LEX_CJK_WORDS__, "../vendors/dict/UTF-8/lex-lang.lex", __LENGTH__ );
    friso_dic_load( friso, config, __LEX_CJK_WORDS__, "../vendors/dict/UTF-8/lex-nation.lex", __LENGTH__ );
    friso_dic_load( friso, config, __LEX_CJK_WORDS__, "../vendors/dict/UTF-8/lex-net.lex", __LENGTH__ );
    friso_dic_load( friso, config, __LEX_CJK_WORDS__, "../vendors/dict/UTF-8/lex-org.lex", __LENGTH__ );
    friso_dic_load( friso, config, __LEX_CJK_WORDS__, "../vendors/dict/UTF-8/lex-touris.lex", __LENGTH__ );

    //__CJK_UNITS__
    friso_dic_load( friso, config, __LEX_CJK_UNITS__, "../vendors/dict/UTF-8/lex-units.lex", __LENGTH__ );
    //__MIX_WORDS__
    friso_dic_load( friso, config, __LEX_ECM_WORDS__, "../vendors/dict/UTF-8/lex-ecmixed.lex", __LENGTH__ );
    //__CEM_WORDS__
    friso_dic_load( friso, config, __LEX_CEM_WORDS__, "../vendors/dict/UTF-8/lex-cemixed.lex", __LENGTH__ );
    //__CN_LNAME__
    friso_dic_load( friso, config, __LEX_CN_LNAME__, "../vendors/dict/UTF-8/lex-lname.lex", __LENGTH__ );
    //__CN_SNAME__
    friso_dic_load( friso, config, __LEX_CN_SNAME__, "../vendors/dict/UTF-8/lex-sname.lex", __LENGTH__ );
    //__CN_DNAME1__
    friso_dic_load( friso, config, __LEX_CN_DNAME1__, "../vendors/dict/UTF-8/lex-dname-1.lex", __LENGTH__ );
    //__CN_DNAME2__
    friso_dic_load( friso, config, __LEX_CN_DNAME2__, "../vendors/dict/UTF-8/lex-dname-2.lex", __LENGTH__ );
    //__CN_LNA__
    friso_dic_load( friso, config, __LEX_CN_LNA__, "../vendors/dict/UTF-8/lex-ln-adorn.lex", __LENGTH__ );
    friso_dic_load( friso, config, __LEX_STOPWORDS__, "../vendors/dict/UTF-8/lex-stopword.lex", __LENGTH__ );
    friso_dic_load( friso, config, __LEX_ENPUN_WORDS__, "../vendors/dict/UTF-8/lex-en-pun.lex", __LENGTH__ );
    friso_dic_load( friso, config, __LEX_EN_WORDS__, "../vendors/dict/UTF-8/lex-en.lex", __LENGTH__ );

    e_time = clock();

    printf("Done, cost: %f sec, size=%d\n", ( double ) ( e_time - s_time ) / CLOCKS_PER_SEC, \
        friso_all_dic_size( friso->dic ) );

    while ( 1 ) {
    printf("friso-%d>> ", lex);
    scanf("%s", _line);
    if ( strcmp( _line, "quit" ) == 0 ) {
        break;
    }  else if ( strcmp( _line, "help" ) == 0 ) {
        ___PRINT_HELP_INFO___
    } else if ( strcmp( _line, "#set" ) == 0 ) {
        printf("lex_t>> ");
        scanf("%d", &lex);
    } else {
        s_time = clock();
        friso_dic_match( friso->dic, lex, _line );
        e = friso_dic_get( friso->dic, lex, _line );
        e_time = clock();
        if ( e != NULL ) {
        printf("word=%s, syn=%s, fre=%d, cost:%fsec\n", 
            e->word, e->syn==NULL? "NULL" : (char *)e->syn->items[0], e->fre, 
            (double) ( e_time - s_time ) / CLOCKS_PER_SEC );
        } else {
        printf("%s was not found.\n", _line);
        }
    }
    }

    //friso_dic_free( friso->dic );
    friso_free(friso);

    return 0;
}
