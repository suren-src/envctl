return {
  {
    "neovim/nvim-lspconfig",
    opts = {
      servers = {
        bufls = {}, -- protobuf
        clangd = {},
        csharp_ls = {},
        dockerls = {},
        elixirls = {},
        html = {},
        jsonls = {},
        jdtls = {},
        tsserver = {},
        kotlin_language_server = {},
        gopls = {},
        pyright = {},
        rust_analyzer = {},
        metals = {},
        sourcekit = {}, --Swift
        sqlls = {},
        yamlls = {},
      },
    },
  },
}
