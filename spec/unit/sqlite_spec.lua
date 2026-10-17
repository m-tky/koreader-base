require("ffi_wrapper")

describe("SQLite", function()
    local sqlite, db

    setup(function()
        sqlite = require("lua-ljsqlite3/init")
    end)

    after_each(function()
        if db then
            db:close()
            db = nil
        end
    end)

    it("should create and query an indexed table on 32-bit builds", function()
        db = sqlite.open(":memory:")
        -- SQLite 3.54.0 with memory statistics disabled overruns the reusable
        -- opcode buffer on ARMhf while preparing these statements.
        db:exec([[
            CREATE TABLE cache (
                key TEXT PRIMARY KEY,
                value BLOB,
                size INTEGER,
                last_access INTEGER
            );
            CREATE INDEX idx_last_access ON cache(last_access);
        ]])
        db:exec("INSERT INTO cache VALUES ('test', 'value', 5, 0);")
        assert.is_equal("value", db:rowexec("SELECT value FROM cache WHERE key = 'test';"))
    end)
end)
