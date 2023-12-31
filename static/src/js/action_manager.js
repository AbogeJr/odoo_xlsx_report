/** @odoo-module */

import { registry } from "@web/core/registry";
import { download } from "@web/core/network/download";
import framework from "web.framework";
import session from "web.session";

registry.category("ir.actions.report handlers").add("xlsx", async (action) => {
  if (action.report_type === "xlsx") {
    framework.blockUI();
    var def = $.Deferred();
    var dd = session.get_file({
      url: "/xlsx_reports",
      data: action.data,
      success: () => {
        console.log("\n\nSuccess!!");
        def.resolve.bind(def);
      },
      error: (error) => {
        console.log("\n\nError\n\n", error);
        // this.call("crash_manager", "rpc_error", error);
      },
      complete: framework.unblockUI,
    });
    return def;
  }
});
