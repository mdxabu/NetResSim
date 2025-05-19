/*
Copyright © 2025 mdxabu

*/
package cmd

import (
	"fmt"

	"github.com/spf13/cobra"
)

// This command used to visualize the ripe atlas results
var visualizeCmd = &cobra.Command{
	Use:   "visualize",
	Short: "",
	Long: ``,
	Run: func(cmd *cobra.Command, args []string) {
		fmt.Println("visualize called")
	},
}

func init() {
	rootCmd.AddCommand(visualizeCmd)
}
