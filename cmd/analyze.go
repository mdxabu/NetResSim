/*
Copyright © 2025 mdxabu

*/
package cmd

import (
	"fmt"

	"github.com/spf13/cobra"
)

var analyzeCmd = &cobra.Command{
	Use:   "analyze",
	Short: "",
	Long: ``,
	Run: func(cmd *cobra.Command, args []string) {
		fmt.Println("analyze called")
	},
}

func init() {
	rootCmd.AddCommand(analyzeCmd)
}
