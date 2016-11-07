# tagbar2
tagbar for my needs

add this in .vimrc file.
```vimscript
function! Tag2Start()
    silent execute "! echo ". expand("%:p") ." > ~/.vim/plugins/tagbar2/curr_info"
    let t2_line=getline('.')                                  
    silent execute "! echo \'".t2_line."\' >> ~/.vim/plugins/tagbar2/curr_info" 
    silent execute "! pwd >> ~/.vim/plugins/tagbar2/curr_info"
    silent execute "! python ~/.vim/plugins/tagbar2/main.py "
	let t2_file=readfile('/home/teja/.vim/plugins/tagbar2/read_file')
	153     execute " sp /home/teja/.vim/plugins/tagbar2/chetta/".t2_file[0]
	154     execute "vsp /home/teja/.vim/plugins/tagbar2/chetta/".t2_file[1]
	155     execute "vsp /home/teja/.vim/plugins/tagbar2/chetta/".t2_file[2]
endfunction
nnoremap <leader>2 <Esc>:silent execute ':call Tag2Start()'<cr>mqVggG<Esc>`q<Esc>
```

and clone into ~/.vim/plugins/ folder
