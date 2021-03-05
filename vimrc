" General{{{
" set nocompatible: disable vi but not vim
set nocp

" handle filetype
filetype on
filetype off

" delete key effect
set backspace=eol,indent,start

" mouse position
set mouse=a

" disable backup
set nobk " nobackup
set noswapfile

" undodir
set undodir=~/.vim/undodir

" specific
set ar " autoread: automatically read which have been changed
set clipboard+=unnamed
set completeopt=longest,menu,preview,
set hls " hlsearch: highlight search result
set noeb " noerrorbells
set wmnu " wildmenu: enhanced command-line completion

" foldmethod
set fdm=marker " use marker in comment as foldmethod

" commentstring
set cms="#\ %s" " use # as default commentstring
au FileType c setlocal cms="\\ %s"
au FileType markdown setlocal cms="<!-- %s -->"
"}}}

" Vundle{{{
" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
    Plugin 'VundleVim/Vundle.vim' " Self

    Plugin 'mattn/emmet-vim'
    Plugin 'preservim/nerdtree'
    Plugin 'preservim/nerdcommenter'
    Plugin 'tpope/vim-commentary'
call vundle#end()

" set diff indent for filetype
filetype indent on

" enable plugin
filetype plugin on
filetype plugin indent on
" }}}

" Language{{{
set enc=utf-8 " encoding
set fenc=utf-8 " fileencoding
" set fencs=utf-8,chinese,latin-1,gb18030 " fileencodings
" set tenc=utf-8,chinese,latin-1,gb18030 " termencoding
set ff=unix " fileformat

" console message encoding
language message zh_CN.utf-8

" line number
set nu

" indent
set ci
set et
set sts=4
set sw=4
set ts=4

" smart match
set ai
set showmatch
set smartcase
" }}}

" GUI{{{
" set color scheme
set background=dark
colo evening " colorscheme

" gvim menu encoding
source $VIMRUNTIME/delmenu.vim
source $VIMRUNTIME/menu.vim

" set font
set gfn=Consolas:h16:cANSI:qDRAFT " guifont

" guioptions default: egmrLtT(Windows) aegimrLtT(GTK,Motif,Athena)
set go-=e " gui tab
set go-=r " right-hand scrollbar
set go-=t " tearoff menu items
set go-=L " left-hand scrollbar
set go-=T " toolbar

" highlight
set cul " cursorline
syntax on

" split
set splitright
set splitbelow

" statusline
set stl=FILE:%F%y%r%=LINE:%l/%L
set ls=2 " laststatus: 2 always
" }}}

" PluginSetting{{{
" NERDTree
try
    au vimenter * NERDTree
    au bufenter * if (winnr("$") == 1 && exists("b:NERDTree") && b:NERDTree.isTabTree()) | q | endif
catch
endtry
" }}}
