Internal and External Linkage in C
==================================
副標: extern/static/inline variable/function

compiling, linking and declaration
----------------------------------
C 在將 source code 轉化為 executable 時, 至少可分為 compile 跟 link 兩個階段.

1. 在 compile 階段把單獨的 c source code translate 成 cpu instructions 組成的 object code.
2. 在 link 階段把所有需要用到的 object code 連結組成一個執行檔 (除了 dynamic linking 以外)

由於 source code 轉換的最重要階段 compiling 時, 無法看到你使用的其他 c source code 跟外部 library 的 source code 及 binary,

所以 C 語言需要在每個 c source file 裡, 標注每個使用到的內部或外部 variable 跟 function 的 type, 才能在 compiling 階段進行 type checking. 

也就是說, C 語言中所有的 variable 跟 function, 在使用前都要有完整的定義, 或者有僅包含 type 的宣告.

也正是因為如此, C 語言甚至要使用 header file 跟額外的 preprocessor, 來幫助使用外部的 c source code 跟 library.

補充, 常見疑惑:

1. 所有的 library 本質上都是一種 object code, 包含 static library 跟 dynamic library.
   除了 dynamic library 的 cpu instructions 要強制符合 relocable(position independent code) 的條件.
   more: 待補 url
2. header file 不會被單獨 compile, header file 只會被 ``#include`` 貼入到其他 c source code 裡, 跟 c source code 一起被 compile 成 object code.

extern and static variable
--------------------------
名詞解釋: 這邊的外部檔案指的是除了自己以外其他的 c source codes, libraries.

extern variable
~~~~~~~~~~~~~~~
當需要使用外部檔案的 variable 時, 需強制宣告該 variable 為 ``extern`` 並且寫上該 variable 的型態.

example
.. code:: cpp

    /* foo.c */
    int a = 10;
    void print_a(void){
        printf("a = %d\n", &a);
    }

    /* main.c */
    extern int a;
    int main(){
        print_a(); // a = 10
        a++;
        print_a(); // a = 11
        a = 100;
        print_a(); // a = 100
    }

比如說在上面的範例, ``main.c`` 中的 ``extern int a`` 便是引用 ``foo.c`` 中的全域變數 ``int a``.

``extern`` 只能引用全域變數.

restriction
"""""""""""
因為是引用已經定義好的變數, 對宣告方式有很嚴格的限制.

1. 型態需跟原型別相同, 不然為 undefined behavior. 以上面範例來說, ``extern double a`` 很顯然是錯的.
2. 不可給初始值(initialized value). 如 ``extern int a = 100`` 很顯然是錯的.

extern usage in header file
"""""""""""""""""""""""""""
一般來說, 我們會用 ``extern`` 去引用別的 library 的全域變數.

通常 library 會把打算讓你引用的變數, 寫到 header file 裡, 讓所有要用的檔案 ``include`` 就能使用了.

拿上面的 example 出來說的話會直接建立一個 ``foo.h`` 給其他檔案如 ``main.c`` 來使用.
.. code:: cpp

    /* foo.h */
    extern int a;

    /* foo.c */
    int a = 10;
    void print_a(void){
        printf("a = %d\n", &a);
    }

    /* main.c */
    #include "foo.h"
    int main(){
        print_a(); // a = 10
        a++;
        print_a(); // a = 11
        a = 100;
        print_a(); // a = 100
    }

而事實上, header file 裡的變數基本上只會有 extern variable.

extern variable example in library
""""""""""""""""""""""""""""""""""
- stdin, stdout, stderr
- errno

extern variable in function
"""""""""""""""""""""""""""
如果在 function 中使用 extern 引用變數, scope 會跟區域變數一樣只在 function 的範圍內.

.. code:: cpp

    // main.c 
    int foo(){
        extern int a;
        ...
    }

    int main(){
        a = 30; // Error!!
    }

static variable
~~~~~~~~~~~~~~~
1. lifetime 為整個程式執行期間, 與全域變數的 lifetime 相同.
2. 變數檔案內部化, 無法被外部檔案直接 access(或者說 link), 也不汙染其他檔案的 namespace(symbol table in C).
   也就是內部連結(internal linkage)的效果.

因為承接著 ``extern``, 先解釋 2. 的內容.

前面說過, 如果 library 要把全域變數給外部檔案用, 通常會在 library 的 header file 裡加上 ``extern``.

不過即使是 library 沒在 header file 裡加上 ``extern`` 的變數,
我們也可以透過在自己的 c source code 裡加上 ``extern`` 來使用 library 的其他變數.

那如果 library 不想把這個變數給其他檔案 access 怎麼辦, 加上 ``static`` 就可以讓變數無法被外部檔案看到, 無法被連接(linkage).

static variable example in library
""""""""""""""""""""""""""""""""""
- lifetime 全開的 variable in function

  - strtok

extern and static function
--------------------------
當需要使用外部檔案的 function 時, 需宣告該 function 的 type, 通常稱為 function prototype.

跟 variable 不同的是, ``extern`` 可加可不加.

同理

1. 將 function prototype 也放在 header file 的原因顯而易見.
2. 不想讓外部使用某 function, 即在 function definition 前面加上 static.

static function example in library
""""""""""""""""""""""""""""""""""
常用情況: library inner function

- `3rd party library - argparse<https://github.com/Cofyc/argparse>`_

    - string prefix comparsing function used in library inner part.

.. code:: cpp

    // argparse.c
    static const char *
    prefix_skip(const char *str, const char *prefix)
    {
        size_t len = strlen(prefix);
        return strncmp(str, prefix, len) ? NULL : str + len;
    }
 
    static int
    prefix_cmp(const char *str, const char *prefix)
    {
        for (;; str++, prefix++)
            if (!*prefix)
                return 0;
            else if (*str != *prefix)
                return (unsigned char)*prefix - (unsigned char)*str;
    }

    // two functions are not in argparse.h

總結
----
- library 本身

    1. variable/function 希望被外部引用: 在 header file 加上該 variable 的 extern 宣告或 function 的 prototype
    2. variable/function 可被外部引用: 在 c source file 該變數宣告時, 不加上 static.
    3. variable/function 不可被外部引用: 在 c source file 該變數宣告時, 加上 static.

- 使用 library 的外部檔案

    1. 對應上面的 1., header file 有的話, include 後即可使用.
    2. 對應上面的 2., 需在本檔案中加上 extern variable 或 function prototype 才可使用. 如果沒有 library 的 source code 則無法使用. 因為無法知道 variable/function 型態.
    3. 對應上面的 3., 在這種情況下無法使用該變數, 不過可以在這個檔案宣告同名變數使用.

.. code:: cpp

    /* just commented */
    /*
     * 1. external linkage, var1/func1
     * 2. can be external linked, var2/func2
     * 3. internal linkage, var3/func3
     */
    /* libfoo.h */
    extern int var1; 

    void func1(void); //

    /* libfoo.c */
    #include "libfoo.h"

    int var1 = 1; // 1. 
    int var2 = 2; 
    static int var3 = 2; //

    // function forward declaration if needed.
    void func2(void); // 2.
    static void func3(void); // 3.

    // function definition
    void func1(void){ // 1.
        printf("func1\n");
    }
    void func2(void){ // 2. can be external linked
        printf("func2\n");
    }
    static void func3(void){ // 3. internal linkage
        printf("func3\n");
    }

    /* main.c */
    #include "libfoo.h"

    extern int var2;  // if using 2.
    void func2(void); // if using 2.

    extern int var3;  // error
    extern void func3(void);  // error

    int main(){
        var1 = 10; // 1. external linkage
        func1();   // 1. external linkage
    }
