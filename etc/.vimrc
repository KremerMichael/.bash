" syntax is good
syntax enable


" Enable 256 colors palette in Gnome Terminal
"if $COLORTERM == 'gnome-terminal'
"    set t_Co=256
"endif

"try
"    colorscheme desert
"catch
"endtry

" No sound or annoying errors
set noerrorbells
set novisualbell
set t_vb=
set tm=500

" tabs and stuff
set tabstop=4 softtabstop=4
set shiftwidth=4
set expandtab
set smartindent

" set numbers i think
set nu
" Add a bit extra margin to the left
set foldcolumn=1

" Don't wrap lines
set nowrap
" Ignore case
set ignorecase
" Acknowledge case
"set smartcase
set noswapfile
set nobackup
set undodir=~/.vim/undodir
set undofile
set incsearch

" Show matching brackets when text indicator is over them
set showmatch 

" color stuff
" set colorcolumn=80
" highlight ColorColumn ctermbg=0 guibg=lightgrey

" setting backgounr
set background=dark

" enable using mouse
set mouse=a

" Turn on the Wild menu
set wildmenu

" Set utf8 as standard encoding and en_US as the standard language
set encoding=utf8

" Use Unix as the standard file type
set ffs=unix,dos,mac

"Always show current position
set ruler

" Configure backspace so it acts as it should act
set backspace=eol,start,indent
set whichwrap+=<,>,h,l

" Height of the command bar
set cmdheight=1

" Ignore compiled files
set wildignore=*.o,*~,*.pyc

""""""""""""""""""""""""""""""
" Status line
""""""""""""""""""""""""""""""
" Always show the status line
set laststatus=2

" Returns true if paste mode is enabled
function! HasPaste()
    if &paste
        return 'PASTE MODE  '
    endif
    return ''
endfunction

" Format the status line
set statusline=\ %{HasPaste()}%F%m%r%h\ %w\ \ CWD:\ %r%{getcwd()}%h\ \ \ Line:\ %l\ \ Column:\ %c
