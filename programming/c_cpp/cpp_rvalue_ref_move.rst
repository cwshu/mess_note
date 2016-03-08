http://stackoverflow.com/a/4986802

- rvalue reference: reference to rvalue and extend lifetime of rvalue (only constant rvalue?)
::
    
    std::vector<int> return_vector(void)
    {
        std::vector<int> tmp {1,2,3,4,5};
        return tmp;
    }

    std::vector<int> &&rval_ref = return_vector();

- move semantic: transfer rvalue to xvalue?

- RVO(return value optimization) & move constructor
::

    std::vector<int> return_vector(void)
    {
        std::vector<int> tmp {1,2,3,4,5};
        return tmp;
    }

    std::vector<int> rval_ref = return_vector();
    // compiler will use RVO if ok
    // OR fall back to vector's move constructor
