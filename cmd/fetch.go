/*
Copyright © 2025 mdxabu

*/
package cmd

import (
	"fmt"

	"github.com/spf13/cobra"
)



var fetchCmd = &cobra.Command{
	Use:   "fetch",
	Short: "",
	Long: ``,
	Run: func(cmd *cobra.Command, args []string) {
		fmt.Println("fetch called")
	},
}

func init() {
	rootCmd.AddCommand(fetchCmd)

}
