# tagbar2
tagbar for my needs

add this in .vimrc file.
```vimscript
function! Tag2Start()
    silent execute "! echo ". expand("%:p") ." > ~/.vim/plugins/tagbar2/curr    _info"
    let t2_line=getline('.')                                  
    silent execute "! echo \'".t2_line."\' >> ~/.vim/plugins/tagbar2/curr_in    fo" 
    silent execute "! pwd >> ~/.vim/plugins/tagbar2/curr_info"
    silent execute "! python ~/.vim/plugins/tagbar2/main.py "
endfunction
nnoremap <leader>2 <Esc>:silent execute ':call Tag2Start()'<cr>mqVggG<Esc>`q    <Esc>
```

and clone into ~/.vim/plugins/ folder
