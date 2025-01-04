-- Options are automatically loaded before lazy.nvim startup
-- Default options that are always set: https://github.com/LazyVim/LazyVim/blob/main/lua/lazyvim/config/options.lua
-- Add any additional options here

vim.opt.expandtab = true -- Use spaces instead of tabs
vim.opt.shiftwidth = 2 -- Size of an indent
vim.opt.tabstop = 2 -- Number of spaces that a <Tab> counts for

-- Keep clipboard synced except for delete/cut
vim.keymap.set({ "n", "v" }, "d", '"_d', { desc = "Delete without storing in clipboard" })
vim.keymap.set({ "n", "v" }, "D", '"_D', { desc = "Delete without storing in clipboard" })
vim.keymap.set({ "n", "v" }, "c", '"_c', { desc = "Change without storing in clipboard" })
vim.keymap.set({ "n", "v" }, "C", '"_C', { desc = "Change without storing in clipboard" })
--vim.keymap.set({ "n", "v" }, "x", '"_x', { desc = "Delete char without storing in clipboard" })

-- Keep system clipboard functionality
vim.opt.clipboard = "unnamedplus"
